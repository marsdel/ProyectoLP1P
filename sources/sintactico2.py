from lexico import tokens
import ply.yacc as yacc

def p_program(p):
    'program : expression'

def p_expression(p):
    'expression : term'

def p_expression_operations(p):
    '''expression : opmate
                | LPAREN opmate RPAREN
                | expression op expression
                | expression op opmate
                | LPAREN opmate RPAREN op expression
                | expression op LPAREN opmate RPAREN
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
    '''opmate : term op term'''
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



def p_expression_bool(p):
    '''expression : expbool
                | LPAREN expbool RPAREN
                | expression opbool expbool
                | expression opbool expression
                | LPAREN expbool RPAREN opbool expression
                | expression opbool LPAREN expbool RPAREN'''

def p_expression_boolvar(p):
    'expression : term opbool term'
    if (type(p[1])==type(p[3])):
        if p[2] == '==':
            p[0] = bool(p[1] == p[3])
        elif p[2] == '!=':
            p[0] = bool(p[1] != p[3])
        elif p[2] == '>':
            p[0] = bool(p[1] > p[3])
        elif p[2] == '>=':
            p[0] = bool(p[1] >= p[3])
        elif p[2] == '<':
            p[0] = bool(p[1] < p[3])
        elif p[2] == '<=':
            p[0] = bool(p[1] <= p[3])
    else:
        p[0] = "Semantic error in input!"

def p_expbool(p):
    '''expbool : boolean opbool boolean'''
    if p[2] == 'and':
        p[0] = bool(p[1] and p[3])
        print(p[0])
        p[0] = "sintaxis Valida"
    elif p[2] == 'or':
        p[0] = bool(p[1] or p[3])
        print(p[0])
        p[0] = "sintaxis Valida"
    else:
        p[0] = "Semantic error in input!"

def p_boolean(p):
    '''boolean : TRUE
            | FALSE'''

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
def p_opbool(p):
    '''opbool : AND
            | OR'''

def p_term(p):
    '''term : NUMBER
            | MINUS NUMBER
            | IDENTIFIER
            | VAR_GLOBAL
            | VAR_INSTANCE
            | VAR_LOCAL'''
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

