import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys

sys.setrecursionlimit(10000)

ops = dict()
# Boolean operations:
ops["=="] = lambda x,y: x == y
ops["!="] = lambda x,y: x != y
ops[">"] = lambda x,y: x > y
ops[">="] = lambda x,y: x >= y
ops["<"] = lambda x,y: x < y
ops["<="] = lambda x,y: x <= y
# Arithmetic operations:
ops['+'] = lambda x,y: x + y
ops['-'] = lambda x,y: x - y
ops['*'] = lambda x,y: x * y
ops['/'] = lambda x,y: x / y
# Arithmetic operations for arrays/vectors:

def apply_op_matrix(op, matrix1, matrix2):
    if isinstance(matrix1[0], list):
        return [[op(matrix1[i][j],matrix2[i][j]) for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    else:
        return [op(matrix1[i], matrix2[i]) for i in range(len(matrix1))]

ops[".+"] = lambda x,y: apply_op_matrix(ops["+"], x, y)
ops[".-"] = lambda x,y: apply_op_matrix(ops["-"], x, y)
ops[".*"] = lambda x,y: apply_op_matrix(ops["*"], x, y)
ops["./"] = lambda x,y: apply_op_matrix(ops["/"], x, y)



def transpose(matrix):
    return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

class Interpreter(object):
    def __init__(self):
        self.current_memory = Memory()
        self.stack = MemoryStack(self.current_memory)

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Int)
    def visit(self, node):
        return node.value

    @when(AST.Float)
    def visit(self, node):
        return node.value

    @when(AST.String)
    def visit(self, node):
        return node.value

    @when(AST.ID)
    def visit(self, node):
        return self.stack.get(node.id)

    @when(AST.Block)
    def visit(self, node):
        for instr in node.instructions:
            self.visit(instr)

    @when(AST.ExpressionsBlock)
    def visit(self, node):
        return [self.visit(expr) for expr in node.expressions]

    @when(AST.Vector)
    def visit(self, node):
        return self.visit(node.values)

    @when(AST.Transposition)
    def visit(self, node):
        array = self.visit(node.expression)
        return transpose(array)

    @when(AST.Opposite)
    def visit(self, node):
        return -1 * self.visit(node.expression)

    @when(AST.Reference)
    def visit(self, node):
        collection = self.visit(node.id)
        index = self.visit(node.index)
        if len(index) == 1:
            return collection[index[0]]
        else:
            return collection[index[0]][index[1]]


    @when(AST.Binary)
    def visit(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return ops[node.operator](left, right)

    @when(AST.Print)
    def visit(self, node):
        expression = self.visit(node.expression)
        print(" ".join([str(x) for x in expression]))

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()

    @when(AST.Return)
    def visit(self, node):
        raise ReturnValueException(self.visit(node.expression))

    @when(AST.Range)
    def visit(self, node):
        first = self.visit(node.first)
        last = self.visit(node.last)
        return [first, last]

    @when(AST.If)
    def visit(self, node):
        condition = self.visit(node.condition)
        if condition:
            self.stack.push(Memory())
            try:
                self.visit(node.true)
                self.stack.pop()
            except ReturnValueException as return_value: 
                self.stack.pop()
                raise ReturnValueException(return_value)
        else:
            self.stack.push(Memory())
            try:
                self.visit(node.false)
                self.stack.pop()
            except ReturnValueException as return_value: 
                self.stack.pop()
                raise ReturnValueException(return_value)


    @when(AST.While)
    def visit(self, node):
        self.stack.push(Memory())
        while self.visit(node.condition):
            try:
                self.visit(node.expression)
            except ReturnValueException as return_value:
                self.stack.pop()
                raise ReturnValueException(return_value)
            except BreakException:
                break
            except ContinueException:
                continue
        self.stack.pop()

    @when(AST.For)
    def visit(self, node):
        self.stack.push(Memory())
        [first, last] = self.visit(node.range)
        self.stack.insert(node.id.id, first)
        while self.visit(node.id) < last:
            try:
                self.visit(node.expression)
                self.stack.set(node.id.id, self.visit(node.id) + 1)
            except ReturnValueException as return_value:
                self.stack.pop()
                raise ReturnValueException(return_value)
            except BreakException:
                break
            except ContinueException:
                continue
        self.stack.pop()
        

    @when(AST.Assign)
    def visit(self, node):
        assign_op = node.type
        value = self.visit(node.value)
        if len(assign_op) == 1:
            self.stack.set(node.id.id, value)
        else:
            op = assign_op[0]
            old_value = self.stack.get(node.id.id)
            self.stack.set(node.id.id, ops[op](old_value, value))
        


    @when(AST.ListAssign)
    def visit(self, node):
        old_array = self.visit(node.id)
        index = self.visit(node.index)
        assign_op = node.type
        value = self.visit(node.value)
        new_array = old_array
        if len(assign_op) == 1:
            if len(index) == 1:
                new_array[index[0]] = value
            else:
                new_array[index[0]][index[1]] = value
            self.stack.set(node.id.id, value)
        else:
            op = assign_op[0]
            if len(index) == 1:
                new_array[index[0]] = ops[op](old_array[index[0]], value)
            else:
                new_array[index[0]][index[1]] = ops[op](old_array[index[0]][index[1]], value)
        self.stack.set(node.id.id, new_array)

    @when(AST.Function)
    def visit(self, node):
        arguments = self.visit(node.argument)
        argument = arguments[0]
        if node.function == "zeros":
            return [[0 for _ in range(argument)] for _ in range(argument)]
        elif node.function == "ones":
            return [[1 for _ in range(argument)] for _ in range(argument)]
        elif node.function == "eye":
            return [[1 if i == j else 0 for i in range(argument)] for j in range(argument)]



