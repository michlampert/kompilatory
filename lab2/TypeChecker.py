from collections import defaultdict
from SymbolTable import *
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
ttype['+'][ARRAY][ARRAY] = ARRAY

# Boolean operators:
for op in ['<', '>', '==', '!=', '<=', '>=']:
    ttype[op][INT][INT] = BOOL
    ttype[op][FLOAT][INT] = ttype[op][INT][FLOAT] = ttype[op][FLOAT][FLOAT] = BOOL

# We can also compare strings and arrays:
for op in ['==', '!=']:
    ttype[op][STRING][STRING] = BOOL
    ttype[op][VECTOR][VECTOR] = BOOL

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
        self.counter_loop = 0

    def print_error(self, node, msg):
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
        # print(node.argument, arg_symbol)
        if node.function not in ['zeros', 'eye', 'ones']: return None
        if len(node.argument.expressions) == 1:
            arg_symbol = self.visit(node.argument.expressions[0])
            if arg_symbol == INT: return ARRAY
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
            return None

    def visit_Assign(self, node):
        symbol = self.visit(node.value)
        self.table.put(node.id.id, symbol)
        print(symbol, node.id.id)
        return symbol

    def visit_Vector(self, node):
        symbols = [self.visit(n) for n in node.values]
        if len(set(symbols)!=1):
            return VECTOR
        return VECTOR

    def visit_Transposition(self, node):
        pass

    def visit_Block(self, node):
        self.table.pushScope("block")
        return self.visit(node.instructions)
        

    def visit_ExpressionsBlock(self, node):
        self.table.pushScope("block")
        print(node.expressions)
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