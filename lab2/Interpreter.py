import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys
#import numpy as np

sys.setrecursionlimit(10000)

ops = dict()
ops['+'] = lambda x,y: x + y
ops['-'] = lambda x,y: x - y
ops['*'] = lambda x,y: x * y
ops['/'] = lambda x,y: x / y


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
        return [self.visit(value) for value in node.values]

    @when(AST.Transposition)
    def visit(self, node):
        array = self.visit(node.expression)
        pass
        #return np.transpose(array)

    @when(AST.Opposite)
    def visit(self, node):
        return -1 * self.visit(node.expression)

    @when(AST.Reference)
    def visit(self, node):
        collection = self.visit(node.id)
        index = self.visit(node.index)
        return collection[index]

    @when(AST.Binary)
    def visit(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        return ops[node.operator](left, right)

    @when(AST.Print)
    def visit(self, node):
        expression = self.visit(node.expression)
        print(expression)

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
        return range(first, last)

    @when(AST.If)
    def visit(self, node):
        condition = self.visit(node.condition)
        # Generalnie trzeba dodać try/catch żeby rozważyć przypadek gdy w ifie jest zwracany wynik
        if condition:
            self.stack.push(Memory())
            self.visit(node.true)
            self.stack.pop()
        else:
            self.stack.push(Memory())
            self.visit(node.false)
            self.pop()


    @when(AST.While)
    def visit(self, node):
        pass

    @when(AST.For)
    def visit(self, node):
        pass

    @when(AST.Assign)
    def visit(self, node):
        pass

    @when(AST.ListAssign)
    def visit(self, node):
        pass

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



