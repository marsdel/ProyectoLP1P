
# Yacc example
import ply.yacc as yacc
from lexico import tokens 
 # Get the token map from the lexer.  This is required.from calclex import tokens

#start Marco Del Rosario
def p_program(p):
    'program : compstmt'

def p_compstmt(p):
    'compstmt : stmt LPAREN term expr RPAREN TIMES LBRACKET term RBRACKET'

def p_stmt(p):
    '''stmt : call do LBRACKET RBRACKET
            | LBRACKET block_var RBRACKET
            | LBRACKET OR_SYMBOL block_var OR_SYMBOL RBRACKET compstmt END
            | UNDEF fname
            | ALIAS fname fname
            | stmt IF expr
            | stmt WHILE expr
            | stmt UNLESS expr
            | stmt UNTIL expr
            | BEGIN LKEY compstmt RKEY
            | END LKEY compstmt RKEY
            | lhs '=' command LBRACKET do LBRACKET OR_SYMBOL block_var OR_SYMBOL RBRACKET compstmt END RBRACKET
            | expr'''

def p_expr(p):
    '''expr : mlhs '=' mrhs
            | RETURN call_args
            | YIELD call_args
            | expr AND expr
            | expr OR expr
            | NOT expr
            | command
            | '!' command
            | ARG'''

def p_call(p):
    'call : function | command'

def p_command(p):
    '''command : operation call_args
            | primary DOT operation call_args
            | primary UNARY_OP operation call_args
            | SUPER call_args'''

def p_function(p):
    '''function : operation LBRACKET LPAREN LBRACKET call_args RBRACKET RPAREN RBRACKET
                | primary DOT operation LPAREN RPAREN
                | primary DOT operation LPAREN LBRACKET RBRACKET RPAREN
                | primary DOT operation LPAREN LBRACKET call_args RBRACKET RPAREN
                | primary UNARY_OP operation LPAREN RPAREN
                | primary UNARY_OP operation LPAREN LBRACKET RBRACKET RPAREN
                | primary UNARY_OP operation LPAREN LBRACKET call_args RBRACKET RPAREN
                | primary DOT operation
                | primary UNARY_OP operation
                | SUPER LPAREN LBRACKET call_args RBRACKET RPAREN
                | SUPER'''

def p_arg(p):
    '''arg : lhs '=' arg
            | lhs op_asgn arg
            | arg '..' arg
            | arg '...' arg
            | arg PLUS arg
            | arg MINUS arg
            | arg TIMES arg
            | arg DIV arg
            | arg MOD arg
            | arg POW arg
            | PLUS arg
            | MINUS arg
            | arg '|' arg
            | arg '^' arg
            | arg '&' arg
            | arg '<=>' arg
            | arg GREATERTHAN arg
            | arg GREATERTHANEQUAL arg
            | arg LESSERTHAN arg
            | arg LESSERTHANEQUAL arg
            | arg EQUAL arg
            | arg '===' arg
            | arg NOTEQUAL arg
            | arg '=~' arg
            | arg '!~' arg
            | '!' arg
            | '~' arg
            | arg '<<' arg
            | arg '>>' arg
            | arg AND arg
            | arg OR arg
            | DEFINED '?' arg
            | primary'''

#end Marco Del Rosario

# start Hector Rizzo 
def p_sentence(p):
    '''sentence : assignment
                | expression
                | loop'''


def p_variable(p):
    '''variable : VAR_GLOBAL
                | VAR_LOCAL
                | VAR_INSTANCE
                | VAR_CLASS'''


def p_primary(p):
    '''primary : LPAREN compstmt RPAREN
                | literal
                | variable
                | primary UNARY_OP identifier
                | UNARY_OP identifier
                | primary LBRACKET RBRACKET
                | primary LBRACKET args RBRACKET
                | LBRACKET RBRACKET
                | LBRACKET args RBRACKET
                | LBRACKET args COMMA RBRACKET
                | LKEY RKEY
                | LKEY args RKEY
                | LKEY assocs RKEY
                | LKEY args COMMA RKEY
                | LKEY assocs COMMA RKEY
                | RETURN
                | RETURN LPAREN RPAREN
                | RETURN LPAREN call_args RPAREN
                | YIELD
                | YIELD LPAREN RPAREN
                | YIELD LPAREN call_args RPAREN
                | DEFINED '?' LPAREN arg LPAREN
                | function
                | function LKEY compstmt LKEY
                | function LKEY OR_SYMBOL OR_SYMBOL compstmt LKEY
                | function LKEY OR_SYMBOL block_var OR_SYMBOL compstmt LKEY
                | IF expr then compstmt END
                | IF expr then compstmt elsif END
                | IF expr then compstmt elsif ELSE compstmt END
                | UNLESS expr then compstmt END
                | UNLESS expr then compstmt ELSE compstmt END
                | WHILE expr do compstmt END
                | UNTIL expr do compstmt END
                | CASE compstmt when END
                | CASE compstmt when ELSE compstmt END
                | FOR block_var IN expr do compstmt END
                | BEGIN compstmt rescue END
                | BEGIN compstmt rescue ELSE compstmt END
                | BEGIN compstmt rescue ENSURE compstmt END
                | BEGIN compstmt rescue ELSE compstmt ENSURE compstmt END
                | CLASS identifier compstmt END
                | CLASS identifier LESSERTHAN identifier compstmt END
                | MODULE identifier compstmt END
                | DEF fname argdecl compstmt END
                | DEF singleton DOT fname argdecl compstmt end
                | DEF singleton UNARY_OP fname argdecl compstmt end'''

    
def p_elsif(p):
    '''elsif : ELSIF expr then compstmt
            | ELSIF expr then compstmt elsif'''

def p_when(p):
    '''when : WHEN when_args then compstmt
            | when WHEN when_args then compstmt'''


def p_rescue(p):
    '''rescue : RESCUE args do compstmt
              | RESCUE do compstmt
              | rescue RESCUE args do compstmt
              | rescue RESCUE do compstmt'''
def p_then(p):
    '''then	 : TERM
            | THEN
		    | TERM THEN'''


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
 