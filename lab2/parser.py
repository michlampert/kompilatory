#!/usr/bin/python

import scan
import ply.yacc as yacc


tokens = scan.tokens

precedence = (
   ("left", 'PLUS', 'MINUS', "DOTADD", "DOTSUB"),
   ("left", 'TIMES',  'DIVIDE', "DOTMUL", "DOTDIV"),
   ("left", "LT", "GT", "NGT", "NLT", "NEQ", "EQ"),
   ("left", "ASSIGN",  "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN"),
   ("right", "TRANSPOSITION"),
   ("nonassoc", 'IFX'),
   ("nonassoc", 'ELSE')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instruction
                | program instruction"""

def p_instruction(p):
    """instruction : for_instruction
                   | while_instruction
                   | if_instruction
                   | LCURL instructions_list RCURL
                   | BREAK SEMICOLON
                   | CONTINUE SEMICOLON
                   | RETURN expression SEMICOLON
                   | expression SEMICOLON

       instructions_list : instructions_list instruction
                         | instruction"""

def p_expression(p):
    """expression : ID
                  | STRING
                  | INTNUM
                  | FLOAT
                  | LSQUARE expressions_list RSQUARE

                  | ID ASSIGN expression
                  | ID ADDASSIGN expression 
                  | ID SUBASSIGN expression
                  | ID MULASSIGN expression
                  | ID DIVASSIGN expression

                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | expression DOTADD expression
                  | expression DOTMUL expression
                  | expression DOTSUB expression
                  | expression DOTDIV expression

                  | expression LT expression
                  | expression GT expression
                  | expression NGT expression
                  | expression NLT expression
                  | expression EQ expression
                  | expression NEQ expression

                  | expression TRANSPOSITION
                  | MINUS expression %prec OPPOSITE

                  | EYE LPAREN expression RPAREN
                  | ONES LPAREN expression RPAREN
                  | ZEROS LPAREN expression RPAREN

       expressions_list: expressions_list, expression
                       | expression 
    """

def p_if_instruction(p):
    """if_instruction : IF LPAREN expression RPAREN instruction %prec IFX
                      | IF LPAREN expression RPAREN instruction ELSE instruction"""

def p_while_instruction(p):
    """while_instruction : WHILE LPAREN expression RPAREN instruction"""

def p_for_instruction(p):
    """range: expression RANGE expression
       for_instruction: FOR ID ASSIGN range instruction"""

def p_print_instruction(p):
    """ print_instruction: PRINT expression """

parser = yacc.yacc()