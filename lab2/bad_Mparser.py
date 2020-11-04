#!/usr/bin/python

import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
   ("left", 'PLUS', 'MINUS', "DOTADD", "DOTSUB"),
   ("left", 'TIMES',  'DIVIDE', "DOTMUL", "DOTDIV"),
   ("left", "LT", "GT", "NGT", "NLT", "NEQ", "EQ"),
   ("left", "ASSIGN",  "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN"),
   ("right", "EYE", "ONES", "ZEROS"),
   ("right", "TRANSPOSITION"),
   ("right", "RANGE"),
   ("right", "OPPOSITE"),
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
                   | print_instruction
                   | LCURL instructions_list RCURL
                   | BREAK SEMICOLON
                   | CONTINUE SEMICOLON
                   | RETURN expression SEMICOLON
                   | expression SEMICOLON

       instructions_list : instructions_list COMMA instruction
                         | instruction"""

def p_boolean_expr(p):
    """boolean_expr : arithmetic_expr LT arithmetic_expr
                    | arithmetic_expr GT arithmetic_expr
                    | arithmetic_expr NGT arithmetic_expr
                    | arithmetic_expr NLT arithmetic_expr
                    | arithmetic_expr EQ arithmetic_expr
                    | arithmetic_expr NEQ arithmetic_expr 
                    | STRING EQ STRING
                    | STRING NEQ STRING"""

def p_arithmetic_expr(p):
    """arithmetic_expr : ID
                       | INTNUM
                       | FLOAT
                       | LSQUARE RSQUARE
                       | LSQUARE arithmetic_list RSQUARE
                       | arithmetic_expr PLUS arithmetic_expr
                       | arithmetic_expr MINUS arithmetic_expr
                       | arithmetic_expr TIMES arithmetic_expr
                       | arithmetic_expr DIVIDE arithmetic_expr
                       | arithmetic_expr DOTADD arithmetic_expr
                       | arithmetic_expr DOTMUL arithmetic_expr
                       | arithmetic_expr DOTSUB arithmetic_expr
                       | arithmetic_expr DOTDIV arithmetic_expr 
                       | arithmetic_expr TRANSPOSITION
                       | MINUS arithmetic_expr %prec OPPOSITE
                       | EYE LPAREN arithmetic_expr RPAREN
                       | ONES LPAREN arithmetic_expr RPAREN
                       | ZEROS LPAREN arithmetic_expr RPAREN
    
       arithmetic_list : arithmetic_list COMMA arithmetic_expr
                       | arithmetic_expr 
       """

def p_assign_expr(p):
    """ assign_expr : ID ASSIGN arithmetic_expr
                    | ID ADDASSIGN arithmetic_expr 
                    | ID SUBASSIGN arithmetic_expr
                    | ID MULASSIGN arithmetic_expr
                    | ID DIVASSIGN arithmetic_expr
                    | ID ASSIGN boolean_expr
                    | ID ASSIGN STRING """

def p_expression(p):
    """expression : assign_expr
                  | arithmetic_expr
                  | boolean_expr
    """

def p_if_instruction(p):
    """if_instruction : IF LPAREN boolean_expr RPAREN THEN instruction %prec IFX
                      | IF LPAREN boolean_expr RPAREN THEN instruction ELSE instruction"""

def p_while_instruction(p):
    """while_instruction : WHILE LPAREN boolean_expr RPAREN instruction"""

def p_for_instruction(p):
    """range : arithmetic_expr RANGE arithmetic_expr
       for_instruction : FOR ID ASSIGN range instruction"""

def p_print_instruction(p):
    """ print_instruction : PRINT arithmetic_expr
                          | PRINT boolean_expr """

parser = yacc.yacc()