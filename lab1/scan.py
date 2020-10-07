import ply.lex as lex

reserved = {
    'if'    : 'IF',
    'then'  : 'THEN',
    'else'  : 'ELSE',
    'while' : 'WHILE',
    "break" : "BREAK",
    "continue" : "CONTINUE",
    "return" : "RETURN",
    "eye" : "EYE",
    "zeros" : "ZEROS",
    "ones" : "ONES",
    "print" : "PRINT"
}

tokens = [  'PLUS',  'MINUS',  'TIMES',  'DIVIDE', 
            "DOTADD", "DOTSUB", "DOTMUL", "DOTDIV",
            "ASSIGN",  "ADDASSIGN", "SUBASSIGN", "MULASSIGN", "DIVASSIGN",
            "LT", "GT", "LTEQ", "GTEQ", "NEQ", "EQ",
            'LPAREN',  'RPAREN' , "LSQUARE", "RSQUARE", "LBOX", "RBOX",
            "RANGE", "TRANSPOSITION", "COMMA", "SEMICOLON",
            'ID',
            'INTNUM', "FLOAT", "STRING" 
            
            ] + list(reserved.values())

literals = [ '+','-','*','/','(',')', "=", "[", "]", "{", "}", ":", "'", ":", ";"]

t_DOTADD = r'\.\+'
t_DOTSUB = r'\.\-'
t_DOTMUL = r'\.\*'
t_DOTDIV = r'\.\/'

t_ADDASSIGN = r'\+\='
t_SUBASSIGN = r'\-\='
t_MULASSIGN = r'\*\='
t_DIVASSIGN = r'\/\='

t_LT = r"\<"
t_GT = r"\>"
t_LTEQ = r"\<\="
t_GTEQ = r"\>\="
t_NEQ = r"\!\="
t_EQ = r"\=\="


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t


def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTNUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"[a-zA-Z_0-9 \-]*\"'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

t_ignore = '  \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t) :
    print("Illegal character '%s', line %d" %(t.value[0], t.lineno))
    t.lexer.skip(1)

lexer = lex.lex()
fh = open("input.txt", "r");
lexer.input( fh.read() )

output = ""

for token in lexer:
    print("(%d): %s(%s)" %(token.lineno, token.type, token.value))
    output += "(%d): %s(%s)\n" %(token.lineno, token.type, token.value)

print("\nTest: " + "OK" if output == open("pattern.txt").read() else "FAIL")
