
# Yacc example
import ply.yacc as yacc
from lexico import tokens 
 # Get the token map from the lexer.  This is required.from calclex import tokens

# start Hector Rizzo 
def p_sentence(p):
    '''sentence : assignment
                | expression
                | loop'''

def p_assignment(p):
    ''' assignment: variable 
    '''

def p_variable(p):
    '''variable: VAR_GLOBAL
                |VAR_LOCAL
                |VAR_INSTANCE
                |VAR_CLASS'''
    
def p_loop_while(p):
    'loop : WHILE expression do expression END'

def p_do(p):
    '''do : term
        | DO
		| term DO'''
def p_term(p):
    'term : TERM'


# End Hector Rizzo 

def p_expression_plus(p):
     'expression : expression PLUS term'
     p[0] = p[1] + p[3]
 
def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]
 
def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
 
def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]
 
def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]
 
def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
 
def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]
 
def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]
 
# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
 
# Build the parser
parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)
 