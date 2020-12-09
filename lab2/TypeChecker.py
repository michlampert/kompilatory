from collections import defaultdict

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
            return symbol.type
        else:
            self.print_error(node, f"{node.id} is undefined!")
            return None

    def visit_Function(self, node):
        arg_symbol = self.visit(node.argument)
        if node.function not in ['zeros', 'eye', 'ones']: return None
        if arg_symbol == INT: return ARRAY
        return None
            
    def visit_Binary(self, node):
        pass

    def visit_Assign(self, node):
        pass

    def visit_If(self, node):
        pass

    def visit_While(self, node):
        self.counter_loop += 1
        condition_symbol = self.visit(node.condition)
        if condition_symbol != BOOL: self.print_error(node, f"Condition has to evaluate to boolean - got {condition_symbol}!")
        # TODO: Visit block of code:
        
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
        # TODO: Visit block of code:

        self.counter_loop -= 1
        return None

    def visit_Print(self, node):
        self.visit(node.expression)
        return None

    def visit_Return(self, node):
        self.visit(node.expression)
        self.print_error(node, "RETURN has to be inside function definition!")
        return None
    
    def visit_Break(self, node):
        if self.counter_loop == 0: self.print_error(node, "BREAK has to be inside of loop!")
        return None

    def visit_Continue(self, node):
        if self.counter_loop == 0: self.print_error(node, "CONTINUE has to be inside of loop!")
        return None