# Yacc example
import ply.yacc as yacc
from lexico import tokens 
 # Get the token map from the lexer.  This is required.from calclex import tokens
# variable que guarda la salida de la GUI 
resultado = ""

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
                    | defined
                    | boolean_operations
                    | math_operations'''

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
    '''prints : print
                | puts'''

def p_print(p):
    ''' print : PRINT expression
                | PRINT LPAREN expression RPAREN'''
    global resultado 
    resultado = "expresión print correcta"

def p_puts(p):
    ''' puts : PUTS expression
                | PUTS LPAREN expression RPAREN'''
    global resultado 
    resultado = "expresión puts correcta"
    

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
    global resultado
    resultado = "asignacion de variable correcta"

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
                        | BEGIN
                        | END
                        | case'''
                        # TODO
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
    global resultado 
    resultado = "expresión if correcta"

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

def p_case(p):
    ''' case : CASE expression END
            | CASE expression when END
            | CASE expression else END
            | CASE expression when else END'''

def p_when(p):
    ''' when : WHEN it_expression THEN expression
            | WHEN it_expression THEN expression when
            | WHEN it_expression expression
            | WHEN it_expression expression when '''

def p_it_expression(p):
    ''' it_expression : expression
                        | expression it_expression'''


def p_and(p):
    'and : expression AND expression'

def p_or(p):
    'or : expression OR expression'

def p_not(p):
    '''not : NOT expression
            | NOT_SYMBOL expression
            | expression NOTEQUAL expression
            | expression OPPOSITE_MATCHED_STRINGS_OP expression'''

def p_range_expressions(p):
    '''range_expressions : expression RANGE_INCLUSIVE expression
                        | expression RANGE_EXCLUSIVE expression'''

def p_while(p):
    '''while : WHILE expression expression END
            | WHILE expression DO expression END'''
    global resultado 
    resultado = "expresión while correcta"

def p_while_modifier(p):
    'while_modifier : expression WHILE expression'

def p_until(p):
    '''until : UNTIL expression DO expression END
            |  UNTIL expression expression END'''

def p_until_modifier(p):
    'until_modifier : expression UNTIL expression'

def p_iterator(p):
    '''iterator : expression DO OR_SYMBOL expression OR_SYMBOL expression END
                | expression LKEY OR_SYMBOL expression OR_SYMBOL expression RKEY'''

def p_for(p):
    '''for : FOR IDENTIFIER IN expression DO expression END
        | FOR IDENTIFIER IN expression expression END'''
    
    global resultado 
    resultado = "expresión for correcta"

def p_yield(p):
    '''yield : YIELD LPAREN expression RPAREN
            | YIELD expression'''

def p_begin_expression(p):
    '''begin_expression : BEGIN expression END
                        | BEGIN expression RESCUE expression END
                        | BEGIN expression ENSURE expression END
                        | BEGIN expression RESCUE expression ENSURE expression END
                        | BEGIN expression RESCUE expression ELSE expression END
                        | BEGIN expression ELSE expression ENSURE expression END
                        | BEGIN expression RESCUE expression ELSE expression ENSURE expression END'''

def p_retry(p):
    'retry : RETRY'

def p_return(p):
    '''return : RETURN
            | RETURN args_method'''

def p_break(p):
    'break : BREAK'

def p_next(p):
    'next : NEXT'

def p_redo(p):
    'redo : REDO'

def p_begin(p):
    '''begin : BEGIN LKEY expression RKEY'''

def p_end(p):
    '''end : END RKEY expression LKEY'''
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

def p_math_operations(p):
    '''math_operations : expression PLUS expression
                        | expression MINUS expression
                        | expression TIMES expression
                        | expression DIVIDE expression
                        | expression MOD expression
                        | expression POW expression
                        | NUMBER PLUS NUMBER
                        | NUMBER MINUS NUMBER
                        | NUMBER TIMES NUMBER
                        | NUMBER DIVIDE NUMBER
                        | NUMBER MOD NUMBER
                        | NUMBER POW NUMBER
    '''
    # Semantic (prueba semantica)
    global resultado
    if not isinstance(p[1], int) and not isinstance(p[2], int) :

        resultado = "error semantico"
    else:
        resultado = "semantica correcta!"

def p_boolean_operations(p):
    '''boolean_operations : expression AND expression
                        | expression OR expression
                        | expression EQUAL expression
                        | expression NOTEQUAL expression
                        | expression GREATERTHAN expression
                        | expression GREATERTHANEQUAL expression
                        | expression LESSERTHAN expression
                        | expression LESSERTHANEQUAL expression
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
                        | TRUE NOTEQUAL TRUE
    '''
    if p[1] == "true" and p[3] == "true":
        p[1]=p[3]=True
    if p[1] == "false" and p[3] == "false":
        p[1]=p[3]=False
    if p[1] == "true" and p[3] == "false":
        p[1]=True
        p[3]=False
    if p[1] == "false" and p[3] == "true":
        p[1]=False
        p[3]=True
    # Semantic (prueba semantica)
    global resultado
    if p[2] == 'AND':
        p[0] = p[1] and p[3]
        resultado = p[0]
        print(resultado)
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
    global resultado 
    resultado = "expresión incorrecta"
 
# # Build the parser
parser = yacc.yacc()
 
# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print("Sintaxis Valida")

# GUI 
from tkinter import *
from tkinter import ttk, font
import getpass

# Gestor de geometría (pack)

class Aplicacion():

    resultado = ''
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Acceso")
        
     
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
        # la ventana. 
                                         
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
        global resultado
        self.clave.set(resultado)   # aqui se pone el valor de resultado en la caja de texto
 
            
def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()

#End Hector Rizzo

