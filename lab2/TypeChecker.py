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
            print(f"{node.id} - undefined!")
            return None

    # TODO: uwzgledniac rozmiar i typ macierzy
    def visit_Function(self, node):
        self.visit(node.argument)
        if node.function not in ['zeros', 'eye', 'ones']: return None
        if isinstance(node.argument, AST.Int): return ARRAY
        return None
            
    def visit_Binary(self, node):
        pass

    def visit_Assign(self, node):
        pass

    def visit_If(self, node):
        pass

    def visit_While(self, node):
        pass

    def visit_Range(self, node):
        pass

    def visit_For(self, node):
        pass