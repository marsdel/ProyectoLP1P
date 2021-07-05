# Yacc example
import ply.yacc as yacc
from lexico import tokens 
import sys

# Get the token map from the lexer.  This is required.from calclex import tokens

#start Marco Del Rosario
def p_program(p):
    'program : compstmt'
    p[0] = p[1]

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
            | math_operations
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

#Hector Rizzo#
def p_math_operations(p):
    '''math_operations : arg PLUS arg
                        | arg MINUS arg
                        | arg TIMES arg
                        | arg DIVIDE arg
                        | arg MOD arg
                        | arg POW arg
                        | NUMBER PLUS NUMBER
                        | NUMBER MINUS NUMBER
                        | NUMBER TIMES NUMBER
                        | NUMBER DIVIDE NUMBER
                        | NUMBER MOD NUMBER
                        | NUMBER POW NUMBER
    '''
    # Semantic (prueba semantica)
    if not isinstance(p[1], int) and not isinstance(p[2], int) :
        print("Semantic error in input!")
#End Hector Rizzo

#Start Marco Del Rosario
def p_boolean_operations(p):
    '''boolean_operations : arg AND arg
                        | arg OR arg
                        | arg EQUAL arg
                        | arg NOTEQUAL arg
                        | arg GREATERTHAN arg
                        | arg GREATERTHANEQUAL arg
                        | arg LESSERTHAN arg
                        | arg LESSERTHANEQUAL arg
                        | NUMBER EQUAL NUMBER
                        | NUMBER NOTEQUAL NUMBER
                        | NUMBER GREATERTHAN NUMBER
                        | NUMBER GREATERTHANEQUAL NUMBER
                        | NUMBER LESSERTHAN NUMBER
                        | NUMBER LESSERTHANEQUAL NUMBER
                        | TRUE AND TRUE
                        | TRUE OR TRUE
                        | TRUE AND FALSE
                        | TRUE OR FALSE
                        | FALSE AND FALSE
                        | FALSE OR FALSE
                        | TRUE EQUAL TRUE
    '''
    # Semantic (prueba semantica)
    if p[2] == 'AND':
        p[0] = p[1] and p[3]

    elif p[2] == 'OR':
        p[0] = p[1] or p[3]
    elif p[2] == 'EQUAL':
        if p[1] == p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'NOTEQUAL':
        if p[1] != p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'GREATERTHAN':
        if p[1] > p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'GREATERTHANEQUAL':
        if p[1] >= p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'LESSERTHAN':
        if p[1] < p[3]:
            p[0] = True
        else:
            p[0] = False
    elif p[2] == 'LESSERTHANEQUAL':
        if p[1] <= p[3]:
            p[0] = True
        else:
            p[0] = False

    if not isinstance(p[1], bool) and not isinstance(p[2], bool) :
        print("Semantic error in input!")

#End Marco Del Rosario

#Jhossias Calderon
def p_conditions(p):
    '''conditions : arg IF arg
                    | arg ELSE arg
                    | arg ELSIF arg
                    | arg CASE arg 
                    | arg UNLESS arg
                    | STRING IF STRING
                    | STRING ELSE STRING
                    | STRING ELSIF STRING
                    | STRING CASE STRING
                    | STRING UNLESS STRING
    '''

    if not isinstance(p[1], str) and not isinstance(p[2], str) :
        print("Semantic error in input!")

def p_methods_datastructure(p):
    '''methods_datastructure : arg EACH arg
                            | arg SORT arg
                            | arg LENGTH arg
                            | arg FIRST arg
                            | arg LAST arg
    '''
    if not isinstance(p[1], str) and not isinstance(p[2], str) :
        print("Semantic error in input!")

#End Jhossias Calderon

# Error rule for syntax errors ( prueba sintaxis)
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

#!/usr/bin/env python
# -*- coding: utf-8 -*-




#Hector Rizzo
'''from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometría (pack)

class Aplicacion():
    resultado = ''
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
        
        # Cambia el formato de la fuente actual a negrita para
        # resaltar las dos etiquetas que acompañan a las cajas
        # de entrada. (Para este cambio se ha importado el  
        # módulo 'font' al comienzo del programa):
        
        fuente = font.Font(weight='bold')
        
        # Define las etiquetas que acompañan a las cajas de
        # entrada y asigna el formato de fuente anterior: 
                               
        self.etiq1 = ttk.Label(self.raiz, text="Validar expresión:", 
                               font=fuente)
        self.etiq2 = ttk.Label(self.raiz, text="Resultado:", 
                               font=fuente)
        
        # Declara dos variables de tipo cadena para contener
        # el usuario y la contraseña: 
        
        self.usuario = StringVar()
        self.clave = StringVar()
        
        # Realiza una lectura del nombre de usuario que 
        # inició sesión en el sistema y lo asigna a la
        # variable 'self.usuario' (Para capturar esta
        # información se ha importando el módulo getpass
        # al comienzo del programa):
        
        
        # Define dos cajas de entrada que aceptarán cadenas
        # de una longitud máxima de 30 caracteres.
        # A la primera de ellas 'self.ctext1' que contendrá
        # el nombre del usuario, se le asigna la variable
        # 'self.usuario' a la opción 'textvariable'. Cualquier
        # valor que tome la variable durante la ejecución del
        # programa quedará reflejada en la caja de entrada.
        # En la segunda caja de entrada, la de la contraseña,
        # se hace lo mismo. Además, se establece la opción
        # 'show' con un "*" (asterisco) para ocultar la 
        # escritura de las contraseñas:
        
        self.ctext1 = ttk.Entry(self.raiz, 
                                textvariable=self.usuario, 
                                width=30)
        self.ctext2 = ttk.Entry(self.raiz, 
                                textvariable=self.clave, 
                                width=30)
        self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
        
        # Se definen dos botones con dos métodos: El botón
        # 'Aceptar' llamará al método 'self.aceptar' cuando
        # sea presionado para validar la contraseña; y el botón
        # 'Cancelar' finalizará la aplicación si se llega a
        # presionar:
        
        self.boton1 = ttk.Button(self.raiz, text="Aceptar", 
                                 command=self.aceptar)
        self.boton2 = ttk.Button(self.raiz, text="Cancelar", 
                                 command=quit)
                                 
        # Se definen las posiciones de los widgets dentro de
        # la ventana. Todos los controles se van colocando 
        # hacia el lado de arriba, excepto, los dos últimos, 
        # los botones, que se situarán debajo del último 'TOP':
        # el primer botón hacia el lado de la izquierda y el
        # segundo a su derecha.
        # Los valores posibles para la opción 'side' son: 
        # TOP (arriba), BOTTOM (abajo), LEFT (izquierda)
        # y RIGHT (derecha). Si se omite, el valor será TOP
        # La opción 'fill' se utiliza para indicar al gestor
        # cómo expandir/reducir el widget si la ventana cambia
        # de tamaño. Tiene tres posibles valores: BOTH
        # (Horizontal y Verticalmente), X (Horizontalmente) e 
        # Y (Verticalmente). Funcionará si el valor de la opción
        # 'expand' es True.
        # Por último, las opciones 'padx' y 'pady' se utilizan
        # para añadir espacio extra externo horizontal y/o 
        # vertical a los widgets para separarlos entre sí y de 
        # los bordes de la ventana. Hay otras equivalentes que
        # añaden espacio extra interno: 'ipàdx' y 'ipady':
                                         
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True, 
                         padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True, 
                         padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        
        # Cuando se inicia el programa se asigna el foco
        # a la caja de entrada de la contraseña para que se
        # pueda empezar a escribir directamente:
                
        self.ctext2.focus_set()
        
        self.raiz.mainloop()
    
    # El método 'aceptar' se emplea para validar la 
    # contraseña introducida. Será llamado cuando se 
    # presione el botón 'Aceptar'. Si la contraseña
    # coincide con la cadena 'tkinter' se imprimirá
    # el mensaje 'Acceso permitido' y los valores 
    # aceptados. En caso contrario, se mostrará el
    # mensaje 'Acceso denegado' y el foco volverá al
    # mismo lugar.

    
    
    def aceptar(self):
        result = parser.parse(self.ctext1.get())
        print(result)
        self.clave.set(result)

            # Se inicializa la variable 'self.clave' para
            # que el widget 'self.ctext2' quede limpio.
            # Por último, se vuelve a asignar el foco
            # a este widget para poder escribir una nueva
            # contraseña.
            
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()'''

#End Hector Rizzo
 

#Jhossias Calderon
