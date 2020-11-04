import scanner
import ply.yacc as yacc


tokens = scanner.tokens

precedence = (
   ('left', '=', "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN"),
   ("left", '+', '-', "DOTADD", "DOTSUB"),
   ("left", '*', '/', "DOTMUL", "DOTDIV"),
   ("left", "LT", "GT", "NGT", "NLT", "NEQ", "EQ"),
   ("right", 'ONES', 'ZEROS', 'EYE'),
   ("right", "OPP"),
   ("left", "'"),
   ("left", ":"),
   ("nonassoc", 'IFX'),
   ("nonassoc", 'ELSE')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """
    program : instruction
            | program instruction
    """

def p_instruction(p):
    """
    instruction : for_instruction
                | while_instruction
                | if_instruction
                | print_instruction
                | '{' instructions_list '}'
                | BREAK ';'
                | CONTINUE ';'
                | RETURN expression ';'
                | expression ';'
    """

def p_instructions_list(p):
    """
    instructions_list : instruction
                      | instructions_list instruction
    """

# TODO w sekcji z przypisywaniem ID czy expression ?
def p_expression(p):
    """
    expression : ID
               | INTNUM
               | FLOAT
               | STRING
 
               | '(' expression ')' 
 
               | '[' ']'
               | '[' expression_list ']'
 
               | ID '=' expression       
               | ID ADDASSIGN expression
               | ID SUBASSIGN expression 
               | ID MULASSIGN expression
               | ID DIVASSIGN expression
               | ID '[' expression_list ']' '=' expression       
               | ID '[' expression_list ']' ADDASSIGN expression
               | ID '[' expression_list ']' SUBASSIGN expression 
               | ID '[' expression_list ']' MULASSIGN expression
               | ID '[' expression_list ']' DIVASSIGN expression
 
               | ZEROS '(' expression_list ')'
               | ONES '(' expression_list ')'
               | EYE '(' expression_list ')'
 
               | expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
               | expression DOTADD expression
               | expression DOTSUB expression
               | expression DOTMUL expression
               | expression DOTDIV expression
               | '-' expression %prec OPP
 
               | expression '\\\''
               
               | expression EQ expression
               | expression NEQ expression
               | expression LT expression
               | expression NLT expression
               | expression GT expression
               | expression NGT expression
    """ 

def p_expression_list(p):
    """
    expression_list : expression
                    | expression_list ',' expression
    """

def p_if_instruction(p):
    """
    if_instruction : IF '(' expression ')' instruction %prec IFX
                   | IF '(' expression ')' instruction ELSE instruction
    """

def p_while_instruction(p):
    """
    while_instruction : WHILE '(' expression ')' instruction
    """

def p_for_instruction(p):
    """
    range : expression ':' expression
    for_instruction : FOR ID '=' range instruction
    """

def p_print_instruction(p):
    """
    print_instruction : PRINT expression_list ';'
    """


parser = yacc.yacc()