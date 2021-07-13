# Yacc example
import ply.yacc as yacc
from lexico import tokens 
 # Get the token map from the lexer.  This is required.from calclex import tokens

#start Marco Del Rosario
def p_program(p):
    'program : expression'

def p_expression(p):
    '''expression : string_literals
                    | prints
                    | variable
                    | array
                    | hash
                    | method_invocation
                    | super
                    | assignment
                    | expression_operations
                    | control_structure             
                    | class_definitions
                    | singleton_class_definitions
                    | module_definitions
                    | method_definitions
                    | singleton_method_definitions
                    | alias
                    | undef
                    | defined'''

def p_variable(p):
    '''variable : VAR_GLOBAL
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

def p_prints(p):
    '''prints : PRINT expression '''
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

def p_function(p):
    '''function : IDENTIFIER LPAREN RPAREN
                | IDENTIFIER LPAREN args_method RPAREN'''
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
    '''control_structure : if
                        | if_modifier
                        | unless
                        | unless_modifier
                        | and
                        | or
                        | not
                        | range_expressions
                        | while
                        | while_modifier
                        | until
                        | until_modifier
                        | iterator
                        | for
                        | yield
                        | begin_expression
                        | retry
                        | return
                        | break
                        | next
                        | redo
                        | begin
                        | end'''
                        # TODO
                        # | case
                        # | raise TODO'''


def p_if(p):
    '''if : IF expression expression END
            | IF expression THEN expression END
            | IF expression expression elsif END
            | IF expression THEN expression elsif END
            | IF expression expression else END
            | IF expression THEN expression else END
            | IF expression expression elsif else END
            | IF expression THEN expression elsif else END'''

def p_elsif(p):
    '''elsif : ELSIF expression expression END
            | ELSIF expression THEN expression END'''
def p_else(p):
    '''else : ELSE expression'''
    
def p_if_modifier(p):
    'if_modifier : expression IF expression'

def p_unless(p):
    '''unless : UNLESS expression expression END
            | UNLESS expression THEN expression END
            | UNLESS expression THEN expression else END'''

def p_unless_modifier(p):
    '''unless_modifier : expression UNLESS expression'''

def p_and(p):
    'and : expression AND expression'

def p_or(p):
    'or : expression OR expression'

def p_not(p):
    '''not : NOT expression
            | NOT_SYMBOL expression'''

def p_range_expressions(p):
    '''range_expressions : expression RANGE_INCLUSIVE expression
                        | expression RANGE_EXCLUSIVE expression'''

def p_while(p):
    'while : WHILE expression expression DO expression END'

def p_while_modifier(p):
    'while_modifier : expression WHILE expression'

def p_until(p):
    'until : UNTIL expression DO expression END'

def p_until_modifier(p):
    'until_modifier : expression UNTIL expression'

def p_iterator(p):
    '''iterator : expression do OR_SYMBOL expression OR_SYMBOL expression END
                | expression LKEY OR_SYMBOL expression OR_SYMBOL expression RKEY'''

def p_for(p):
    'for : FOR expression IN expression DO expression END'

def p_yield(p):
    '''yield : YIELD LPAREN expression RPAREN
            | YIELD expression'''

def p_begin_expression(p):
    '''begin_expression : BEGIN expression RESCUE expression ENSURE expression END
                        | BEGIN expression RESCUE expression ELSE expression ENSURE expression END'''

def p_retry(p):
    'retry : RETRY'

def p_return(p):
    '''return : RETURN
            | RETURN expression'''

def p_break(p):
    'break : BREAK'

def p_next(p):
    'next : NEXT'

def p_redo(p):
    'redo : REDO'

def p_begin(p):
    'begin : BEGIN LKEY expression RKEY'

def p_end(p):
    'end : END LKEY expression RKEY'

#definitions-------------------------------
def p_class_definitions(p):
    '''class_definitions : CLASS IDENTIFIER expression END
                        | CLASS IDENTIFIER LESSERTHAN SUPER expression END'''

def p_singleton_class_definitions(p):
    'singleton_class_definitions : CLASS BINARY_LEFT_SHIFT_OP expression expression END'

def p_module_definitions(p):
    'module_definitions : MODULE IDENTIFIER expression END'

def p_method_definitions(p):
    '''method_definitions : DEF function expression END'''

def p_singleton_method_definitions(p):
    '''singleton_method_definitions : DEF expression DOT IDENTIFIER expression END
                        | DEF expression DOT IDENTIFIER LPAREN args_method RPAREN expression END'''

def p_alias(p):
    'alias : ALIAS expression expression'

def p_undef(p):
    'undef : UNDEF expression'

def p_defined(p):
    'defined : DEFINED_OP expression'


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
