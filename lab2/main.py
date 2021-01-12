import sys
import ply.yacc as yacc
from Mparser import parser
import scanner
from TreePrinter import TreePrinter
from TypeChecker import TypeChecker
from Interpreter import Interpreter

if __name__ == '__main__':

    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else "lab2/example9.m"
        file = open(filename, "r")
    except IOError:
        print("Cannot open {0} file".format(filename))
        sys.exit(0)

    text = file.read()
    ast = parser.parse(text, lexer=scanner.lexer)
    typeChecker = TypeChecker()   
    typeChecker.visit(ast)
    if typeChecker.error_counter == 0:
        interpreter = Interpreter()
        interpreter.visit(ast)