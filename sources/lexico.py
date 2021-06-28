from typing import DefaultDict
import ply.lex as lex

#Autor: Marco Del Rosario
#Ingreso de palabras reservadas
# List of token names.   This is always required
reserved = {
    'alias' : 'ALIAS', 'and' : 'AND',
    'break' : 'BREAK', 'begin' : 'BEGIN',
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
    'POW',
    #variables +Hector Rizzo
    'VAR_GLOBAL',
    'VAR_INSTANCE',
    'VAR_CLASS',
    'VAR_LOCAL',
    'VAR_SYSTEM',

    'STRING',
    'TERM',
    'CASE_EQUALITY',
    'COMBINED_COMPARISON_OP',
    'EXPONENT_AND',
    'RANGE_INCLUSIVE',
    'RANGE_EXCLUSIVE',
    'BINARY_XOR_OP',
    'BINARY_AND_OP',
    'MATCHED_STRINGS_OP',
    'OPPOSITE_MATCHED_STRINGS_OP',
    'BINARY_LEFT_SHIFT_OP',
    'BINARY_RIGHT_SHIFT_OP',
    'DEFINED_OP',
    'COMPLEMENT_OP',
    'OVERLOAD_PLUS',
    'OVERLOAD_MINUS',

    'HASH_ROCKET',
    'IDENTIFIER',
    'UNARY_OP',
    'LBRACKET',
    'RBRACKET',
    'LKEY',
    'RKEY',
    'COMMA',
    'DOT',
    'OR_SYMBOL',
    'NOT_SYMBOL',
    'EQUAL_SYMBOL',
    'OPTIONAL_SYMBOL',
    # END Hector Rizzo
    # start Marco Del Rosario
    'PLUS_EQUAL',
    'MINUS_EQUAL',
    'TIMES_EQUAL',
    'DIVIDE_EQUAL',
    'MOD_EQUAL',
    'POW_EQUAL',
	'SINGLE_AND_EQUAL',
    'SINGLE_OR_EQUAL',
    'XOR_EQUAL',
    'BINARY_LEFT_EQUAL',
    'BINARY_RIGHT_EQUAL',
	'AND_EQUAL',
    'OR_EQUAL',
    #end Marco Del Rosario
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
t_POW = r'\*\*'
t_EQUAL = r'\=\='
t_NOTEQUAL = r'\!\='
t_GREATERTHAN = r'\>'
t_GREATERTHANEQUAL = r'\>\='
t_LESSERTHAN = r'\<'
t_LESSERTHANEQUAL = r'\<\='

#Marco Del Rosario
t_PLUS_EQUAL = r'\+='
t_MINUS_EQUAL = r'-='
t_TIMES_EQUAL = r'\*='
t_DIVIDE_EQUAL = r'/='
t_MOD_EQUAL = r'\%='
t_POW_EQUAL = r'\*\*='
t_SINGLE_AND_EQUAL = r'&='
t_SINGLE_OR_EQUAL = r'\|='
t_XOR_EQUAL = r'\^='
t_BINARY_LEFT_EQUAL = r'\<\<='
t_BINARY_RIGHT_EQUAL = r'\>\>='
t_AND_EQUAL = r'&&='
t_OR_EQUAL = r'\|\|='

#Hector Rizzo
t_CASE_EQUALITY = r'==='
t_COMBINED_COMPARISON_OP = r'\<=\>'
t_EXPONENT_AND = r'\*\*='
t_BINARY_XOR_OP = r'\^'
t_BINARY_AND_OP = r'&'
t_MATCHED_STRINGS_OP = r'=\~'
t_OPPOSITE_MATCHED_STRINGS_OP = r'\!\~'
t_OVERLOAD_PLUS = r'\+\@'
t_OVERLOAD_MINUS = r'-\@'
t_HASH_ROCKET = r'=>'
t_RANGE_INCLUSIVE = r'\.\.'
t_RANGE_EXCLUSIVE = r'\.\.\.'
t_UNARY_OP = r'::'
t_LBRACKET = r'\['
t_RBRACKET = r']'
t_LKEY = r'\{'
t_RKEY = r'\}'
t_COMMA = r','
t_DOT = r'\.'
t_OR_SYMBOL = r'\|'
t_NOT_SYMBOL = r'\!'
t_EQUAL_SYMBOL = r'='
t_OPTIONAL_SYMBOL = r'\?'
t_BINARY_LEFT_SHIFT_OP = r'\<\<'
t_BINARY_RIGHT_SHIFT_OP = r'\>\>'
t_COMPLEMENT_OP = r'~'
t_DEFINED_OP = r'defined\?'


#Simbolo Jhossias Calderon
t_SYMBOL = r':\w+'

#variables +Hector Rizzo
t_VAR_GLOBAL = r'\$\w+'
t_VAR_INSTANCE = r'\@\w+'
t_VAR_CLASS = r'\@\@\w+'
t_VAR_SYSTEM = r'\$[!|@|_|.|&|~|n|=|/|\\|0|*|$|?]'
t_STRING = r'"\w+"|\'\w+\'|´\w+´'
t_VAR_LOCAL =r'((_[a-z]+)|[a-z])\w*'
t_TERM= r';|\n'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved words
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

'''
linea=" "
while linea!="":
    linea=input(">>")
    lexer.input(linea)
    getTokens(lexer)
# Tokenize
print("Succesfull")
'''