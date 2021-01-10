import AST

def addToClass(cls):
    def decorator(func):
        setattr(cls,func.__name__,func)
        return func
    return decorator

class TreePrinter:

    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Int)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.value))

    @addToClass(AST.Float)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.value))

    @addToClass(AST.String)
    def printTree(self, indent=0):
        print("|  " * indent + self.value)

    @addToClass(AST.ID)
    def printTree(self, indent=0):
        print("|  " * indent + str(self.id))

    @addToClass(AST.Block)
    def printTree(self, indent=0):
        for i in self.instructions: i.printTree(indent)

    @addToClass(AST.ExpressionsBlock)
    def printTree(self, indent=0):
        for i in self.expressions: i.printTree(indent)
    
    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        print("|  " * indent + "VECTOR")
        for v in self.values:
            v.printTree(indent + 1)

    @addToClass(AST.Transposition)
    def printTree(self, indent=0):
        print("|  " * indent + "TRANSPOSE")
        self.expression.printTree(indent + 1)

    @addToClass(AST.Opposite)
    def printTree(self, indent=0):
        print("|  " * indent + "OPPOSITE")
        self.expression.printTree(indent + 1)

    @addToClass(AST.Reference)
    def printReference(self, ident=0):
        print("|  " * indent + "REFERENCE")
        self.id.printTree(ident + 1)
        for e in self.expressions:
            e.printTree(ident+1)

    @addToClass(AST.Function)
    def printTree(self, indent=0):
        print("|  " * indent + self.function)
        self.argument.printTree(indent + 1)
        
    @addToClass(AST.Binary)
    def printTree(self, indent=0):
        print("|  " * indent + self.operator)
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.Assign)
    def printTree(self, indent=0):
        print("|  " * indent + self.type)
        self.id.printTree(indent + 1)
        self.value.printTree(indent + 1)

    @addToClass(AST.ListAssign)
    def printTree(self, indent=0):
        print("|  " * indent + self.type)
        self.id.printTree(indent + 1)
        self.index.printTree(indent + 1)
        self.value.printTree(indent + 1)

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        print("|  " * indent + "RETURN")
        self.expression.printTree(indent + 1)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        print("|  " * indent + "BREAK")

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        print("|  " * indent + "CONTINUE")

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        print("|  " * indent + "PRINT")
        self.expression.printTree(indent + 1)

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        print("|  " * indent + "RANGE")
        self.first.printTree(indent + 1)
        self.last.printTree(indent + 1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        print("|  " * indent + "FOR")
        self.id.printTree(indent + 1)
        self.range.printTree(indent + 1)
        self.expression.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        print("|  " * indent + "WHILE")
        self.condition.printTree(indent + 1)
        self.expression.printTree(indent + 1)

    @addToClass(AST.If)
    def printTree(self, indent=0):
        print("|  " * indent + "IF")
        self.condition.printTree(indent + 1)
        print("|  " * indent + "THEN")
        self.true.printTree(indent + 1)
        if self.false != AST.Block([]):
            print("|  " * indent + "ELSE")
            self.false.printTree(indent + 1)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        print("| " * indent + "Error")