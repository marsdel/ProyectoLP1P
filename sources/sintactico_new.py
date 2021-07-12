# Yacc example
import ply.yacc as yacc
from lexico import tokens 
 # Get the token map from the lexer.  This is required.from calclex import tokens

#start Marco Del Rosario
def p_program(p):
    'program : compstmt'

def p_expressions(p):
    '''expression : string_literals
                    | variables
                    | array
                    | hash
                    | method_invocation
                    | super
                    | assignment
                    | expression_operations
                    | control_structure             
                    | Class definitions
                    | Singleton-class definitions
                    | Module definitions
                    | Method definitions
                    | Singleton-method definitions
                    | alias
                    | undef
                    | defined?'''

def p_variables(p):
    '''variables : VAR_GLOBAL
                    | VAR_INSTANCE
                    | VAR_CLASS
                    | VAR_LOCAL
                    | VAR_SYSTEM 
                    | VAR_CONSTANT'''

def p_string_literals(p):
    '''string_literals : STRING
                        | string_concat '''

def p_string_concat(p):
    ''' string_concat : DOUBLE_QUOTED IDENTIFIER concat DOUBLE_QUOTED
                        | DOUBLE_QUOTED IDENTIFIER concat IDENTIFIER DOUBLE_QUOTED '''

def p_concat(p):
    '''concat : NUMBER_SIGN LKEY IDENTIFIER RKEY'''

def p_array(p):
    '''array : LBRACKET args_array RBRACKET'''

def p_array_data(p):
    '''array_data : IDENTIFIER LBRACKET NUMBER RBRACKET'''

def p_args_array(p):
    '''args_array : data
                    | data COMMA args_array'''

def p_hash(P):
    '''hash : LKEY args_hash RKEY'''

def p_args_hash(p):
    '''args_hash : data HASH_ROCKET data
                | data HASH_ROCKET data COMMA args_hash'''

#[expr `.'] identifier [`(' expr...[`*' [expr]],[`&' ] expr`)']
#[expr `::'] identifier [`(' expr...[`*' [expr]],[`&' expr] `)']

def p_function(p):
    '''function : IDENTIFIER LPAREN RPAREN'''
def p_super(p):
    '''super : SUPER LPAREN RPAREN
            | SUPER LPAREN args_method RPAREN'''

def p_method_invocation(p):
    '''method_invocation : IDENTIFIER DOT IDENTIFIER LPAREN RPAREN
                        | IDENTIFIER DOT IDENTIFIER LPAREN args_method RPAREN
                        | IDENTIFIER DOT IDENTIFIER'''

def p_args_method(p):
    '''args_method : data
                | data COMMA args_method'''

    # variable '=' expr
    # constant '=' expr
    # expr`['expr..`]' '=' expr
    # expr`.'identifier '=' expr
def p_assignment(p):
    '''assignment : variable EQUAL_SYMBOL data
                    | array_data EQUAL_SYMBOL data
                    | method_invocation EQUAL_SYMBOL data 
                    | self_assigment
                    | mult_assigment'''

def p_self_assigment(p):
    '''self_assigment : variable op_assigment data'''

def p_op_assigment(p):
    '''op_assigment : PLUS_EQUAL
                    | MINUS_EQUAL
                    | TIMES_EQUAL
                    | DIVIDE_EQUAL
                    | MOD_EQUAL
                    | POW_EQUAL'''

def p_mult_assigment(p):
    '''mult_assigment : list_var EQUAL_SYMBOL args_method'''

def p_list_var(p):
    '''list_var : variable COMMA
                | variable COMMA list_var
                | variable'''


def p_control_structure(p):
    '''control_structure : if'''
                        # TODO
                        # | if modifier
                        # | unless
                        # | unless modifier
                        # | case
                        # | and
                        # | or
                        # | not
                        # | Range expressions
                        # | while
                        # | while modifier
                        # | until
                        # | until modifier
                        # | Iterators
                        # | for
                        # | yield
                        # | raise
                        # | begin
                        # | retry
                        # | return
                        # | break
                        # | next
                        # | redo
                        # | BEGIN
                        # | END TODO'''


def p_if(p):
    '''if : IF expression expression END
            | IF expression THEN expression END
            | IF expression expression elsif END
            | IF expression THEN expression elsif END
            | IF expression expression else END
            | IF expression THEN expression else END
            | IF expression expression elsif else END
            | IF expression THEN expression elsif else END'''

def p_elseif(p):
    '''elseif : '''


def p_expression_operations(p):
    '''expression_operations : opmate
                            | LPAREN opmate RPAREN
                            | expression_operations op expression_operations
                            | expression_operations op opmate
                            | LPAREN opmate RPAREN op expression_operations
                            | expression_operations op LPAREN opmate RPAREN
                '''
    if (len(p) > 2):
        if (p[1] != "Semantic error in input!" and p[3] != "Semantic error in input!"):
            if p[2] == '+':
                p[0] = (p[1] + p[3])
            elif p[2] == '-':
                p[0] = (p[1] - p[3])
            elif p[2] == '*':
                p[0] = (p[1] * p[3])
            elif p[2] == '/':
                p[0] = (p[1] / p[3])
            elif p[2] == '%':
                p[0] = (p[1] % p[3])
        else:
            p[0] = "Semantic error in input!"
    else:
        if (p[1] == "Semantic error in input!"):
            p[0] = "Semantic error in input!"
        else:
            p[0] = "sintaxis Valida"
            print(p[0])

def p_opmate(p):
    '''opmate : data op data'''
    if (len(p) > 2):
        if (p[1] != "Semantic error in input!" and p[3] != "Semantic error in input!"):
            if p[2] == '+':
                p[0] = (p[1] + p[3])
            elif p[2] == '-':
                p[0] = (p[1] - p[3])
            elif p[2] == '*':
                p[0] = (p[1] * p[3])
            elif p[2] == '/':
                p[0] = (p[1] / p[3])
            elif p[2] == '%':
                p[0] = (p[1] % p[3])
        else:
            p[0] = "Semantic error in input!"
    else:
        if (p[1] == "Semantic error in input!"):
            p[0] = "Semantic error in input!"
        else:
            print(p[0])
            p[0] = "sintaxis Valida"

def p_op(p):
    '''op : PLUS
        | MINUS
        | TIMES
        | DIVIDE
        | MOD
        | EQUAL
        | NOTEQUAL
        | GREATERTHAN
        | GREATERTHANEQUAL
        | LESSERTHAN
        | LESSERTHANEQUAL
    '''

def p_data(p):
    '''data : NUMBER
            | STRING
            | variable'''


#Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!", p)
 
# Build the parser
parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print("Sintaxis Valida")
