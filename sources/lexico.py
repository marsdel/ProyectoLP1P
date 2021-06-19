from typing import DefaultDict
import ply.lex as lex
# List of token names.   This is always required
reserved = {
    'if' : 'IF',
    'then' : 'THEN',
    'else' : 'ELSE',
    'while' : 'WHILE',
}
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'MOD',
    'ID',
    'VARGBL',
    'VARINST',
    'VARCLASS',
    'VARLOCAL',
) + tuple(reserved.values())
# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'\%'
t_VARGBL = r'\$\w+'
t_VARINST = r'\@\w+'
t_VARCLASS = r'\@\@\w+'
t_VARLOCAL = r'_\w+'

def t_ID(t):
    r'[a-zA-Z_]\w+'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)



# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)



# Build the lexer
lexer = lex.lex()


data= ''' 
$ere
$AR
@ar
@@ar
@aef
_ar
ar
'''
lexer.input(data)

while True:
    tok =lexer.token()
    if not tok:
        break
    print(tok)