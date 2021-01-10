import scanner
import ply.yacc as yacc
import AST


tokens = scanner.tokens

precedence = (
   ("left", "LT", "GT", "NGT", "NLT", "NEQ", "EQ"),
   ("left", '+', '-', "DOTADD", "DOTSUB"),
   ("left", '*', '/', "DOTMUL", "DOTDIV"),
   ('left', '=', "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN"),
   ("nonassoc", 'ONES', 'ZEROS', 'EYE'),
   ("nonassoc", "OPP"),
   ("nonassoc", 'TRANSPOSITION'),
   ("nonassoc", ":"),
   ("nonassoc", 'IFX'),
   ("nonassoc", 'ELSE')
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")

# --------------- PROGRAM: ------------------------

def p_program(p):
    """
    program : instruction
    """
    p[0] = AST.Block(p.lineno(1), [p[1]])

def p_program_block(p):
    """ 
    program : program instruction
    """
    program = p[1]
    program.instructions.append(p[2])
    p[0] = program 

# --------------- INSTRUCTIONS: --------------------

def p_expression_instruction(p):
    "instruction : expression ';'"
    p[0] = p[1]

def p_break_instruction(p):
    """ 
    instruction : BREAK ';'
    """
    p[0] = AST.Break(p.lineno(1))

def p_continue_instruction(p):
    """ 
    instruction : CONTINUE ';'
    """
    p[0] = AST.Continue(p.lineno(1))

def p_return_instruction(p):
    """ 
    instruction : RETURN expression ';'
    """
    p[0] = AST.Return(p.lineno(1), p[2])

def p_instructions_list(p):
    """
    instructions_list : instruction
    """
    p[0] = AST.Block(p.lineno(1), [p[1]])

def p_instructions(p):
    """
    instructions_list : instructions_list instruction
    """
    instructions_list = p[1]
    instructions_list.instructions.append(p[2])
    p[0] = instructions_list

def p_block_instruction(p):
    """
    instruction : '{' instructions_list '}'
    """
    p[0] = p[2]

# --------------- EXPRESSIONS: --------------------

def p_expression_nest(p):
    """
    expression : '(' expression ')'
    """ 
    p[0] = p[2]

def p_expression_empty_vector(p):
    """
    expression : '[' ']'
    """
    p[0] = AST.Vector(p.lineno(1), [])

def p_expression_vector(p):
    """
    expression : '[' expression_list ']'
    """
    p[0] = AST.Vector(p.lineno(1), p[2]) #AST.Vector(p[2])

def p_expression_int(p):
    """
    expression : INTNUM
    """
    p[0] = AST.Int(p.lineno(1), p[1])

def p_expression_float(p):
    """
    expression : FLOAT
    """
    p[0] = AST.Float(p.lineno(1), p[1])

def p_expression_id(p):
    """
    expression : ID
    """
    p[0] = AST.ID(p.lineno(1), p[1])

def p_expression_string(p):
    """
    expression : STRING
    """
    p[0] = AST.String(p.lineno(1), "\"" + p[1] + "\"")

def p_expression_transposition(p):
    """
    expression : expression TRANSPOSITION
    """
    p[0] = AST.Transposition(p.lineno(1), p[1])

def p_expression_opposite(p):
    """
    expression : '-' expression %prec OPP
    """
    p[0] = AST.Opposite(p.lineno(1), p[2])

def p_expression_function(p):
    """
    expression : ZEROS '(' expression_list ')'
               | ONES '(' expression_list ')'
               | EYE '(' expression_list ')'
    """
    p[0] = AST.Function(p.lineno(1), p[1], p[3])

def p_expression_assign(p):
    """
    expression : ID '=' expression       
                 | ID ADDASSIGN expression
                 | ID SUBASSIGN expression 
                 | ID MULASSIGN expression
                 | ID DIVASSIGN expression
    """
    p[0] = AST.Assign(p.lineno(1), p[2], AST.ID(p.lineno(1), p[1]), p[3])

def p_expression_list_assign(p):
    """
    expression : ID '[' expression_list ']' '=' expression       
               | ID '[' expression_list ']' ADDASSIGN expression
               | ID '[' expression_list ']' SUBASSIGN expression 
               | ID '[' expression_list ']' MULASSIGN expression
               | ID '[' expression_list ']' DIVASSIGN expression
    """
    p[0] = AST.ListAssign(p.lineno(1), p[5], AST.ID(p.lineno(1), p[1]), p[3], p[6])

def p_expression_array_reference(p):
    """
    expression : ID '[' expression_list ']'
    """
    p[0] = AST.Reference(p.lineno(1), AST.ID(p.lineno(1), p[1]),  p[3])

def p_expression_binary(p):
    """ 
    expression : expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
               | expression DOTADD expression
               | expression DOTSUB expression
               | expression DOTMUL expression
               | expression DOTDIV expression
               | expression EQ expression
               | expression NEQ expression
               | expression LT expression
               | expression NLT expression
               | expression GT expression
               | expression NGT expression
    """
    p[0] = AST.Binary(p.lineno(1), p[2], p[1], p[3])

def p_expression_list(p):
    """
    expression_list : expression
    """
    p[0] = AST.ExpressionsBlock(p.lineno(1), [p[1]])

def p_expressions(p):
    """
    expression_list : expression_list ',' expression
    """
    expression_list = p[1]
    expression_list.expressions.append(p[3])
    p[0] = expression_list

# --------------- SPECIAL INSTRUCTIONS: --------------------

def p_if_else_instruction(p):
    """
    instruction : IF '(' expression ')' instruction ELSE instruction
    """
    p[0] = AST.If(p.lineno(1), p[3], p[5], p[7])

def p_if_instruction(p):
    """
    instruction : IF '(' expression ')' instruction %prec IFX
    """
    p[0] = AST.If(p.lineno(1), p[3], p[5])

def p_while_instruction(p):
    """
    instruction : WHILE '(' expression ')' instruction
    """
    p[0] = AST.While(p.lineno(1), p[3], p[5])

def p_range(p):
    """
    range : expression ':' expression
    """
    p[0] = AST.Range(p.lineno(1), p[1], p[3])

def p_for_instruction(p):
    """
    instruction : FOR ID '=' range instruction
    """
    p[0] = AST.For(p.lineno(1), AST.ID(p.lineno(1), p[2]), p[4], p[5])


def p_print_instruction(p):
    """
    instruction : PRINT expression_list ';'
    """
    p[0] = AST.Print(p.lineno(1), p[2])


parser = yacc.yacc()