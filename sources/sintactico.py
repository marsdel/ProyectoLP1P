
# Yacc example
import ply.yacc as yacc
from lexico import tokens 
 # Get the token map from the lexer.  This is required.from calclex import tokens

#start Marco Del Rosario
def p_program(p):
    'program : compstmt'

'STMT (TERM EXPR)* [TERM]'
def p_compstmt(p):
    '''compstmt : stmt
                | stmt term
                | stmt term expr term'''

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
            | NOT_SYMBOL command
            | arg'''

def p_call(p):
    '''call : function 
        | command'''

def p_command(p):
    '''command : operation call_args
            | primary DOT operation call_args
            | primary UNARY_OP operation call_args
            | SUPER call_args'''

def p_function(p):
    '''function : operation LBRACKET LPAREN LBRACKET call_args RBRACKET RPAREN RBRACKET
                | primary DOT operation LPAREN call_args RPAREN
                | primary UNARY_OP operation LPAREN call_args RPAREN
                | primary DOT operation
                | primary UNARY_OP operation
                | SUPER LPAREN call_args RPAREN
                | SUPER'''

def p_arg(p):
    '''arg : lhs '=' arg
            | lhs op_asgn arg
            | arg RANGE_INCLUSIVE arg
            | arg RANGE_EXCLUSIVE arg
            | arg PLUS arg
            | arg MINUS arg
            | arg TIMES arg
            | arg DIVIDE arg
            | arg MOD arg
            | arg POW arg
            | PLUS arg
            | MINUS arg
            | arg OR_SYMBOL arg
            | arg BINARY_XOR_OP arg
            | arg BINARY_AND_OP arg
            | arg COMBINED_COMPARISON_OP arg
            | arg GREATERTHAN arg
            | arg GREATERTHANEQUAL arg
            | arg LESSERTHAN arg
            | arg LESSERTHANEQUAL arg
            | arg EQUAL arg
            | arg CASE_EQUALITY arg
            | arg NOTEQUAL arg
            | arg MATCHED_STRINGS_OP arg
            | arg OPPOSITE_MATCHED_STRINGS_OP arg
            | NOT_SYMBOL arg
            | COMPLEMENT_OP arg
            | arg BINARY_LEFT_SHIFT_OP arg
            | arg BINARY_RIGHT_SHIFT_OP arg
            | arg AND arg
            | arg OR arg
            | DEFINED_OP arg
            | primary'''

#end Marco Del Rosario

# start Hector Rizzo 

def p_variable(p):
    '''variable : VAR_GLOBAL
                | VAR_LOCAL
                | VAR_INSTANCE
                | VAR_CLASS'''


def p_primary(p):
    '''primary : LPAREN compstmt RPAREN
                | literal
                | variable
                | primary UNARY_OP IDENTIFIER
                | UNARY_OP IDENTIFIER
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
                | DEFINED_OP LPAREN arg LPAREN
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
                | CLASS IDENTIFIER compstmt END
                | CLASS IDENTIFIER LESSERTHAN IDENTIFIER compstmt END
                | MODULE IDENTIFIER compstmt END
                | DEF fname argdecl compstmt END
                | DEF singleton DOT fname argdecl compstmt END
                | DEF singleton UNARY_OP fname argdecl compstmt END'''

    
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

def p_when_args(p):
    '''when_args : args 
        | args COMMA TIMES arg
		| TIMES arg'''

def p_then(p):
    '''then	 : TERM
            | THEN
		    | TERM THEN'''

def p_do(p):
    '''do : term
        | DO
		| term DO'''

def p_term(p):
    'term : TERM'

def p_mrhs(p):
    '''mrhs : args
        | args COMMA
        | args TIMES
        | args arg
		| TIMES arg'''

def p_lhs(p):
    '''lhs : variable
		| primary LBRACKET RBRACKET
        | primary LBRACKET args RBRACKET
		| primary DOT IDENTIFIER
    '''

def p_block_var(p):
    '''block_var : lhs
		| mlhs'''

def p_mlhs(p):
    '''mlhs : mlhs_item COMMA mlhs_item TIMES
            | mlhs_item COMMA mlhs_item lhs
            | mlhs_item COMMA mult_mlhs_item TIMES
            | mlhs_item COMMA mult_mlhs_item lhs
            | TIMES lhs

    '''
#TODO *
def p_mult_mlhs_item(p):
    'mult_mlhs_item : COMMA mlhs_item'

def p_mlhs_item(p):
    '''mlhs_item : lhs
		| LPAREN mlhs RPAREN'''

def p_args(p):
    '''args : arg
            | arg COMMA arg'''

def p_argdecl(p):
    '''argdecl : LPAREN arglist RPAREN 
                | arglist term
    '''

def p_arglist(p):
    '''arglist : IDENTIFIER 
                | IDENTIFIER COMMA IDENTIFIER
                | IDENTIFIER COMMA '&' IDENTIFIER
    '''

def p_singleton(p):
    '''singleton : variable 
                | LPAREN expr RPAREN'''

def p_assocs(p):
    '''assocs : assoc
    | assoc COMMA assoc
    '''

def p_assoc(p):
    '''assoc : arg HASH_ROCKET arg
    '''

def p_call_args(p):
    '''call_args : args
                | args COMMA assocs
                | args COMMA TIMES arg
                | args COMMA BINARY_AND_OP arg
                | args COMMA assocs COMMA TIMES arg
                | args COMMA assocs COMMA BINARY_AND_OP arg
                | args COMMA TIMES arg COMMA BINARY_AND_OP arg
                | args COMMA assocs COMMA TIMES arg COMMA BINARY_AND_OP arg
                | assocs
                | assocs COMMA TIMES arg
                | assocs COMMA BINARY_AND_OP arg
                | assocs COMMA TIMES arg COMMA BINARY_AND_OP arg
                | TIMES arg
                | TIMES arg COMMA BINARY_AND_OP arg
                | BINARY_AND_OP arg
                | command
    '''

def p_literal(p):
    '''literal : NUMBER 
                | SYMBOL 
                | STRING
                | IDENTIFIER'''

def p_fname(p):
    '''fname : IDENTIFIER 
            | RANGE_INCLUSIVE 
            | OR_SYMBOL 
            | BINARY_XOR_OP 
            | BINARY_AND_OP
		    | COMBINED_COMPARISON_OP 
            | EQUAL
            | CASE_EQUALITY 
            | MATCHED_STRINGS_OP
            | GREATERTHAN 
            | GREATERTHANEQUAL
            | LESSERTHAN
            | LESSERTHANEQUAL
		    | PLUS
            | MINUS
            | TIMES
            | DIVIDE 
            | MOD 
            | POW
		    | BINARY_LEFT_SHIFT_OP 
            | BINARY_RIGHT_SHIFT_OP
            | COMPLEMENT_OP
            | OVERLOAD_PLUS 
            | OVERLOAD_MINUS
            | LBRACKET RBRACKET 
            | LBRACKET RBRACKET EQUAL_SYMBOL'''

def p_operation(p):
    '''operation : IDENTIFIER
                | IDENTIFIER NOT_SYMBOL
                | IDENTIFIER OPTIONAL_SYMBOL'''

def p_op_asgn(p):
    '''op_asgn : PLUS_EQUAL 
                | MINUS_EQUAL
                | TIMES_EQUAL
                | DIVIDE_EQUAL
                | MOD_EQUAL
                | POW_EQUAL
		        | SINGLE_AND_EQUAL
                | SINGLE_OR_EQUAL
                | XOR_EQUAL 
                | BINARY_LEFT_EQUAL 
                | BINARY_RIGHT_EQUAL
		        | AND_EQUAL 
                | OR_EQUAL'''
# End Hector Rizzo

#Start Marco Del Rosario
def p_fname(p):
    '''fname : IDENTIFIER
            | RANGE_INCLUSIVE
            | OR_SYMBOL
            | BINARY_AND_OP
            | BINARY_XOR_OP
            | COMBINED_COMPARISON_OP
            | EQUAL
            | CASE_EQUALITY
            | MATCHED_STRINGS_OP
            | GREATERTHAN
            | GREATERTHANEQUAL
            | LESSERTHAN
            | LESSERTHANEQUAL
            | PLUS
            | MINUS
            | TIMES
            | DIVIDE
            | MOD
            | POW
            | BINARY_RIGHT_SHIFT_OP
            | BINARY_LEFT_SHIFT_OP
            | COMPLEMENT_OP
            | OVERLOAD_PLUS
            | OVERLOAD_MINUS
            | LBRACKET RBRACKET
            | LBRACKET RBRACKET EQUAL_SYMBOL'''

def p_operation(p):
    '''operation : IDENTIFIER
                | IDENTIFIER NOT_SYMBOL
                | IDENTIFIER OPTIONAL_SYMBOL'''

def p_op_asgn(p):
    '''op_asgn : PLUS_EQUAL
                | MINUS_EQUAL
                | TIMES_EQUAL
                | DIVIDE_EQUAL
                | MOD_EQUAL
                | POW_EQUAL
		        | SINGLE_AND_EQUAL
                | SINGLE_OR_EQUAL
                | XOR_EQUAL
                | BINARY_LEFT_EQUAL
                | BINARY_RIGHT_EQUAL
		        | AND_EQUAL
                | OR_EQUAL'''

#end Marco Del Rosario

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
    print(result)
 