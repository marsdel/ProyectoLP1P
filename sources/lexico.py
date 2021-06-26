from typing import DefaultDict
import ply.lex as lex

#Autor: Marco Del Rosario
#Ingreso de palabras reservadas
# List of token names.   This is always required
reserved = {
    'alias' : 'ALIAS', 'and' : 'AND',
    'break' : 'BREAK', 'begin' : 'begin',
    'case' : 'CASE', 'class' : 'CLASS',
    'def' : 'DEF', 'defined' : 'DEFINED', 'do' : 'DO',
    'else' : 'ELSE', 'elsif' : 'ELSIF', 'end' : 'END', 'ensure' : 'ENSURE',
    'false' : 'FALSE', 'true' : 'TRUE',
    'for' : 'FOR',
    'if' : 'IF', 'in' : 'IN',
    'module' : 'MODULE',
    'next' : 'NEXT', 'nil' : 'NIL', 'not' : 'NOT',
    'or' : 'OR',
    'puts' : 'PUTS',
    'redo' : 'REDO', 'rescue' : 'RESCUE', 'retry' : 'RETRY', 'return' : 'RETURN',
    'self' : 'SELF', 'super' : 'SUPER',
    'then' : 'THEN',
    'undef' : 'UNDEF', 'unless' : 'UNLESS', 'until' : 'UNTIL',
    'when' : 'WHEN', 'while' : 'WHILE',
    'yield' : 'YIELD',
    '_FILE_' : '_FILE_', '_LINE_' : '_LINE_'
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
    #variables +Hector Rizzo
    'VAR_GLOBAL',
    'VAR_INSTANCE',
    'VAR_CLASS',
    'VAR_LOCAL',
    'VAR_SYSTEM',
    # Hector Rizzo
    #Simbolo Jhossias Calderon
    'SYMBOL',
    'EQUAL',
    'NOTEQUAL',
    'GREATERTHAN',
    'GREATERTHANEQUAL',
    'LESSERTHAN',
    'LESSERTHANEQUAL'
) + tuple(reserved.values()) #transformacion a tupla del diccionario +Marco Del Rosario
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_MOD = r'\%'
t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_GREATERTHAN = r'\>'
t_GREATERTHANEQUAL = r'\>\='
t_LESSERTHAN = r'\<'
t_LESSERTHANEQUAL = r'\<\='


#Simbolo Jhossias Calderon
t_SYMBOL = r':\w+'

#variables +Hector Rizzo
t_VAR_GLOBAL = r'\$\w+'
t_VAR_INSTANCE = r'\@\w+'
t_VAR_CLASS = r'\@\@\w+'
t_VAR_SYSTEM = r'\$[!|@|_|.|&|~|n|=|/|\\|0|*|$|?]'

def t_VAR_LOCAL(t):
    r'((_\w+)|[a-z])\w*'
    t.type = reserved.get(t.value, 'VAR_LOCAL')  # Check for reserved words
    return t

# +Hector Rizzo
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

def getTokens(lexer):
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)


# Build the lexer
lexer = lex.lex()

"""
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")
"""