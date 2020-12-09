class VariableSymbol():

    def __init__(self, name, ttype):
        self.name = name
        self.type = ttype


class SymbolTable(object):

    def __init__(self, parent, name): # parent scope and symbol table name
        self.parent = parent
        self.name = name
        self.symbols = {}

    def put(self, name, symbol): # put variable symbol or fundef under <name> entry
        self.symbols[name] = symbol

    def get(self, name): # get variable symbol or fundef from <name> entry
        if name in self.symbols: return self.symbols[name]
        if self.parent: return self.parent.get(name)
        return None

    def getParentScope(self):
        return self.parent
    
    def pushScope(self, name):
        new_scope = SymbolTable(self, name)
        self = new_scope
        
    def popScope(self):
        self = self.parent
    
