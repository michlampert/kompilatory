from collections import defaultdict
from SymbolTable import *
import AST
# ---------------- TYPES -----------------

INT = 'INT'
FLOAT = 'FLOAT'
STRING = 'STRING'
RANGE = 'RANGE'
VECTOR = 'VECTOR'
ARRAY = 'ARRAY'
BOOL = 'BOOL'

# ----------- OPERATION TYPES: -----------

ttype = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: None)))

# Arithmetic operators:
for op in ['+', '-', '*', '/']:
    ttype[op][INT][INT] = INT
    ttype[op][FLOAT][INT] = ttype[op][INT][FLOAT] = ttype[op][FLOAT][FLOAT] = FLOAT

ttype['+'][STRING][STRING] = STRING
ttype['*'][STRING][INT] = STRING
ttype['*'][INT][STRING] = STRING

# Boolean operators:
for op in ['<', '>', '==', '!=', '<=', '>=']:
    ttype[op][INT][INT] = BOOL
    ttype[op][FLOAT][INT] = ttype[op][INT][FLOAT] = ttype[op][FLOAT][FLOAT] = BOOL

# We can also compare strings and arrays:
for op in ['==', '!=']:
    ttype[op][STRING][STRING] = BOOL
    ttype[op][VECTOR][VECTOR] = BOOL

for op in [".+", ".-", ".*", "./"]:
    ttype[op][VECTOR][VECTOR] = BOOL
    ttype[op][ARRAY][ARRAY] = BOOL

class Collection:
    def __init__(self, type, size):
        self.type = type
        self.size = size

class NodeVisitor(object):

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)


    def generic_visit(self, node):        # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)

    # simpler version of generic_visit, not so general
    #def generic_visit(self, node):
    #    for child in node.children:
    #        self.visit(child)



class TypeChecker(NodeVisitor):

    def __init__(self):
        self.table = SymbolTable(None, "table")
        # We want to check if BREAK/CONTINUE is inside loop:
        self.error_counter = 0
        self.counter_loop = 0

    def print_error(self, node, msg):
        self.error_counter += 1
        print(f"LINE {node.line}: {msg}")

    def visit_Int(self, node):
        return INT

    def visit_Float(self, node):
        return FLOAT
    
    def visit_String(self, node):
        return STRING
 
    def visit_ID(self, node):
        symbol = self.table.get(node.id)
        if symbol:
            return symbol
        else:
            self.print_error(node, f"{node.id} is undefined!")
            return None

    def visit_Function(self, node):
        if node.function not in ['zeros', 'eye', 'ones']: return None
        if node.function == 'eye':
            if len(node.argument.expressions) == 1:
                arg_symbol = self.visit(node.argument.expressions[0])
                arg_value = node.argument.expressions[0].value
                if arg_symbol == INT: return Collection(ARRAY, [arg_value, arg_value])
        else:
            if len(node.argument.expressions) == 1:
                arg_symbol = self.visit(node.argument.expressions[0])
                arg_value = node.argument.expressions[0].value
                if arg_symbol == INT: return Collection(VECTOR, arg_value)
            if len(node.argument.expressions) == 2:
                arg_symbol1 = self.visit(node.argument.expressions[0])
                arg_symbol2 = self.visit(node.argument.expressions[1])
                arg_value1 = node.argument.expressions[0].value
                arg_value2 = node.argument.expressions[1].value
                if arg_symbol1 == INT and arg_symbol2 == INT: return Collection(ARRAY, [arg_value1, arg_value2])
        self.print_error(node, f'Bad arguments for function: {node.function}')
        return None
            
    def visit_Binary(self, node):
        left_symbol = self.visit(node.left)
        right_symbol = self.visit(node.right)
        operator = node.operator
        if operator[0] != '.':
            bin_symbol = ttype[operator][left_symbol][right_symbol]
            if bin_symbol is None: self.print_error(node, f'Mismatched types for {operator}, with {left_symbol} and {right_symbol}')
            return bin_symbol
        else:
            if isinstance(left_symbol, Collection) and isinstance(right_symbol, Collection):
                if left_symbol.type == right_symbol.type and left_symbol.size == right_symbol.size: return left_symbol
            else: 
                self.print_error(node, f'Mismatched types for {operator}, with {left_symbol.type} and {right_symbol.type}')
            return None

    def visit_Assign(self, node):
        symbol = self.visit(node.value)
        self.table.put(node.id.id, symbol)
        #print(symbol, node.id.id)
        return symbol

    def visit_Vector(self, node):
        symbols = [self.visit(n) for n in node.values.expressions]
        len_ith_symbol = lambda i: len(node.values.expressions[i].values.expressions)
        for i,s in enumerate(symbols):
            if not isinstance(s, Collection) and s != symbols[0]:
                self.print_error(node, f'Mismatched types for: {s} and {symbols[0]}!')
            if isinstance(s, Collection) and (not isinstance(symbols[0], Collection) or s.type != symbols[0].type):
                self.print_error(node, f'Mismatched types for: {s} and {symbols[0]}!')
            if isinstance(s, Collection) and s.type == VECTOR:
                if len_ith_symbol(i) != len_ith_symbol(0):
                    self.print_error(node, f'Mismatched size of vectors for: {s} and {symbols[0]}!')
            if isinstance(s, Collection) and s.type == ARRAY:
                self.print_error(node, f'We do not support 3D arrays!')
        if isinstance(s, Collection) and s.type == VECTOR: 
            return Collection(ARRAY, [len(symbols), len_ith_symbol(0)])
        return Collection(VECTOR, len(symbols))

    def visit_Transposition(self, node):
        symbol = self.visit(node.expression) 
        if not isinstance(symbol, Collection) or symbol.type != ARRAY:
            self.print_error(node, f'Only arrays can be transposed!')
        symbol.size[0], symbol.size[1] = symbol.size[1], symbol.size[0]
        return symbol


    def visit_Block(self, node):
        self.table.pushScope("block")
        return self.visit(node.instructions)
        
    def visit_ExpressionsBlock(self, node):
        self.table.pushScope("block")
        #print(node.expressions)
        return self.visit(node.expressions)

    def visit_If(self, node):
        condition_symbol = self.visit(node.condition)
        if condition_symbol != BOOL: self.print_error(node, f'If: got {condition_symbol} instead of Bool as condition.')
        self.table.pushScope("true")
        self.visit(node.true)
        self.table.popScope()
        self.table.pushScope("false")
        self.visit(node.false)
        self.table.popScope()
        return None

    def visit_While(self, node):
        self.counter_loop += 1
        condition_symbol = self.visit(node.condition)
        if condition_symbol != BOOL: self.print_error(node, f"Condition has to evaluate to boolean - got {condition_symbol}!")
        self.table.pushScope("expression")
        self.visit(node.expression)
        self.table.popScope()
        self.counter_loop-=1
        return None

    def visit_Range(self, node):
        first_symbol = self.visit(node.first)
        last_symbol = self.visit(node.last)
        if first_symbol != INT or last_symbol != INT: self.print_error(node, "Range's first and last has to be an integer!")
        return RANGE

    def visit_For(self, node):
        self.counter_loop += 1
        range_symbol = self.visit(node.range)
        if range_symbol != RANGE: self.print_error(node, f"For loop: got {range_symbol} instead of range!")
        self.table.pushScope("expression")
        self.table.put(node.id.id, INT)
        self.visit(node.expression)
        self.table.popScope()
        self.counter_loop -= 1
        return None

    def visit_Print(self, node):
        self.visit(node.expression)
        return None

    def visit_Return(self, node):
        self.visit(node.expression)
        #self.print_error(node, "RETURN has to be inside function definition!")
        return None
    
    def visit_Break(self, node):
        if self.counter_loop == 0: self.print_error(node, "BREAK has to be inside of loop!")
        return None

    def visit_Continue(self, node):
        if self.counter_loop == 0: self.print_error(node, "CONTINUE has to be inside of loop!")
        return None

    def visit_Opposite(self, node):
        opposite_symbol = self.visit(node.expression)
        if opposite_symbol not in [FLOAT, INT]: self.print_error(node, 'Opposite: got {type1} instead of number.')
        return opposite_symbol

    def visit_ListAssign(self, node):
        #print(self.visit(node.id).size)
        id_type = self.visit(node.id)
        expressions = [self.visit(i) for i in node.index.expressions]
        if [e for e in expressions if e != INT and e != RANGE]: self.print_error(node, 'All indexes have to be integers.')
        if not isinstance(id_type, Collection) : self.print_error(node, '{node.id.id} is not a collection.')
        if id_type.type == VECTOR and len(node.index.expressions) > 1:  self.print_error(node, '{node.id.id} is a vector not an array - bad reference.')
        indexes = [index.value for index in node.index.expressions]
        if None not in indexes:
            if len(indexes) == 2:
                if indexes[0] >= id_type.size[0] or indexes[1] >= id_type.size[1]:
                    self.print_error(node, 'Index out of scope.')
            else:
                if indexes[0] >= id_type.size:
                    self.print_error(node, 'Index out of scope.')
        return id_type

    def visit_Reference(self, node):
        id_type = self.visit(node.id)
        expressions = [self.visit(i) for i in node.index.expressions]
        if [e for e in expressions if e != INT and e != RANGE]: self.print_error(node, 'All indexes have to be integers.')
        if not isinstance(id_type, Collection): self.print_error(node, '{node.id.id} is not a collection.')
        if id_type.type == VECTOR and len(node.index.expressions) > 1:  self.print_error(node, '{node.id.id} is a vector not an array - bad reference.')
        indexes = [index.value for index in node.index.expressions]
        if None not in indexes:
            if len(indexes) == 2:
                if indexes[0] >= id_type.size[0] or indexes[1] >= id_type.size[1]:
                    self.print_error(node, 'Index out of scope.')
            else:
                if indexes[0] >= id_type.size:
                    self.print_error(node, 'Index out of scope.')
        return id_type