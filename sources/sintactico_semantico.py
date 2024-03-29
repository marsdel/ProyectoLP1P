# Yacc example
from re import A
import ply.yacc as yacc
from lexico import tokens 

# variable que guarda la salida de la GUI 
resultado = ""

#start Marco Del Rosario
def p_program(p):
    'program : expression'

#diferentes expresiones existentes en el lenguaje propuesto que contienen tipos de datos, estructuras de control,
#estructuras de datos, definicion de clases, entre otras expresiones
def p_expression(p):
    '''expression : string_literals
                    | booleans
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
                    | boolean_operations'''
    p[0] = p[1]

#diferentes variables existentes en el lenguaje propuesto
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
#concatenacion de un string con un identificador
def p_string_concat(p):
    ''' string_concat : DOUBLE_QUOTED IDENTIFIER concat DOUBLE_QUOTED
                        | DOUBLE_QUOTED IDENTIFIER concat IDENTIFIER DOUBLE_QUOTED '''

#concatenacion de un identificador para ser usada en un string
def p_concat(p):
    '''concat : NUMBER_SIGN LKEY IDENTIFIER RKEY'''

def p_prints(p):
    '''prints : print
                | puts'''
#metodo print con las dos opciones a considerar de impresion
def p_print(p):
    ''' print : PRINT expression
                | PRINT LPAREN expression RPAREN'''
    global resultado 
    resultado = "expresión print correcta"

#metodo puts con las dos opciones a considerar de impresion
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

#metodo funcion usado para definir la sintaxis de un metodo real del lenguaje propuesto
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
    global resultado
    resultado = "Invocación de método válido"

def p_args_method(p):
    '''args_method : data
                | data COMMA args_method'''

#metodo de asignaciones donde se puede definir valores a variables definidas en el metodo variable
def p_assignment(p):
    '''assignment : variable EQUAL_SYMBOL data
                    | variable EQUAL_SYMBOL expression_operations
                    | array_data EQUAL_SYMBOL data
                    | method_invocation EQUAL_SYMBOL data 
                    | variable EQUAL_SYMBOL array
                    | variable EQUAL_SYMBOL hash
                    | array_data EQUAL_SYMBOL expression_operations
                    | method_invocation EQUAL_SYMBOL expression_operations
                    | self_assigment
                    | mult_assigment'''
    global resultado
    resultado = "asignacion de variable correcta"

def p_self_assigment(p):
    '''self_assigment : variable op_assigment data'''

#operaciones matematicas existentes en el lenguaje propuesto
def p_op_assigment(p):
    '''op_assigment : PLUS_EQUAL
                    | MINUS_EQUAL
                    | TIMES_EQUAL
                    | DIVIDE_EQUAL
                    | MOD_EQUAL
                    | POW_EQUAL'''

def p_mult_assigment(p):
    '''mult_assigment : list_var EQUAL_SYMBOL args_method'''

#metodo que indica las diferentes formas de listar variables
def p_list_var(p):
    '''list_var : variable COMMA
                | variable COMMA list_var
                | variable'''

#metodo que contiene las diferentes estructuras de control
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
                        

#sintaxis if que valida su segundo parametro como expresion booleana de resultante
def p_if(p):
    '''if : IF expression expression END
            | IF expression THEN expression END
            | IF expression expression elsif END
            | IF expression THEN expression elsif END
            | IF expression expression else END
            | IF expression THEN expression else END
            | IF expression expression elsif else END
            | IF expression THEN expression elsif else END
            | IF boolean_operations'''
    global resultado 
    if(p[2]!=True and p[2] != False):
        resultado ="Condición debe dar un boolean"
    else:
        resultado = "expresión if correcta"
    
#sintaxis elif donde el segundo parametro indica una expresion booleana como resultante
def p_elsif(p):
    '''elsif : ELSIF expression expression END
            | ELSIF expression THEN expression END'''
    global resultado
    if(p[2]!=True and p[2] != False):
        resultado ="Condición de elsif debe dar un boolean"
    else:
        resultado = "expresión if correcta"

def p_else(p):
    '''else : ELSE expression'''
    
def p_if_modifier(p):
    'if_modifier : expression IF expression'
    
#sintaxis unless donde el segundo parametro su expresion tiene que dar un resultado booleano
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

#sintaxis while donde su segundo parametro de constructor su resultante tiene que ser un valor booleano
def p_while(p):
    '''while : WHILE expression expression END
            | WHILE expression DO expression END'''
    global resultado 
    if(p[2]!=True and p[2]!=False):
        resultado = "la condición del while debe dar un boolean"
    else:
        resultado = "expresión while correcta"

def p_while_modifier(p):
    'while_modifier : expression WHILE expression'

def p_until(p):
    '''until : UNTIL expression DO expression END
            |  UNTIL expression expression END'''
    global resultado
    resultado = "Expresión until correcta"

def p_until_modifier(p):
    'until_modifier : expression UNTIL expression'

def p_iterator(p):
    '''iterator : expression DO OR_SYMBOL expression OR_SYMBOL expression END
                | expression LKEY OR_SYMBOL expression OR_SYMBOL expression RKEY'''

#sintaxis de for para realizar el ciclo
def p_for(p):
    '''for : FOR IDENTIFIER IN expression DO expression END
        | FOR IDENTIFIER IN IDENTIFIER DO expression END
        | FOR IDENTIFIER IN IDENTIFIER expression END
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
    
    global resultado
    resultado = "Expresión begin correcta"

def p_retry(p):
    'retry : RETRY'

def p_return(p):
    '''return : RETURN
            | RETURN args_method'''
    
    global resultado
    resultado = "return correcto"

def p_break(p):
    'break : BREAK'
    global resultado
    resultado = "break correcto"


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
        
    global resultado
    resultado = "Definicion de clase correcta"

def p_singleton_class_definitions(p):
    'singleton_class_definitions : CLASS BINARY_LEFT_SHIFT_OP expression expression END'
    global resultado
    resultado = "Definicion de clase correcta"

def p_module_definitions(p):
    'module_definitions : MODULE IDENTIFIER expression END'
    global resultado
    resultado = "Definicion de module correcta"

#sintaxis de metodo a cumplir donde la expression puede ser cualquiera de las anteriores mencionadas
def p_method_definitions(p):
    '''method_definitions : DEF function expression END'''
    global resultado
    resultado = "Definicion de metodo correcta"

def p_singleton_method_definitions(p):
    '''singleton_method_definitions : DEF expression DOT IDENTIFIER expression END
                        | DEF expression DOT IDENTIFIER LPAREN args_method RPAREN expression END'''
    

def p_alias(p):
    'alias : ALIAS expression expression'

    global resultado
    resultado = "Definicion de alias correcta"

def p_undef(p):
    'undef : UNDEF expression'

def p_defined(p):
    'defined : DEFINED_OP expression'

#metodo que implica operadores logicas para obtener resultados booleanos
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
    global resultado
    #condicionales a cumplir para confirmar el uso de booleanos en las operaciones logicas
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
    if p[2] == 'and':
        p[0] = p[1] and p[3]
    elif p[2] == 'or':
        p[0] = p[1] or p[3]

    elif p[2] == '==':
        if p[1] == p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '!=':
        if p[1] != p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '>':
        if p[1] > p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '>=':
        if p[1] >= p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '<':
        if p[1] < p[3]:
            p[0] = True
        else:
            p[0] = False

    elif p[2] == '<=':
        if p[1] <= p[3]:
            p[0] = True
        else:
            p[0] = False
    resultado = "true" if p[0] else "false"

#posibles de operaciones matematicas
def p_expression_operations(p):
    '''expression_operations : opmate
                            | LPAREN opmate RPAREN
                            | expression_operations op expression_operations
                            | expression_operations op opmate
                            | expression_operations op data
                            | LPAREN opmate RPAREN op expression_operations
                            | expression_operations op LPAREN opmate RPAREN
                '''
    p[0] = p[1]

def p_opmate(p):
    '''opmate : data op data'''
        
    global resultado

    #se valida si los valores ingresados en p[1] y p[2] son instancias de enteros para realizar las operaciones respectivas
    if not isinstance(p[1], int) and not isinstance(p[3], int) :
        resultado = "error semantico"
    else:
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
        resultado = p[0]

  
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
    p[0] = p[1]
def p_data(p):
    '''data : NUMBER
            | STRING
            | variable'''
    
    p[0] = p[1]

def p_booleans(p):
    '''booleans : TRUE
                | FALSE'''
    if p[1] == 'true':
        p[0] =True
    else:
        p[0] = False
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
from tkinter import ttk, font, messagebox
import random




# Gestor de geometría (pack)

class Aplicacion():

    #array que contiene diferentes lineas de codigo fuente para probarlas aleatoramiente en la GUI
    array_randoms= [
        '3 + 3',
        'true and true',
        'if 3>4 3+4 end',
        'if a+3 end',
        'true and a',
        'while 3 3+4 end',
        'while true puts("ciclo") end',
        'a + 5',
        '@var = "hello world!!!"',
        '$var = { 3 => 3 , "a" => 3}',
        '$var = { 3 => }',
        '$var = [ 3 => 3 , "a" => 3]',
        '$var = [1,2,3]',
        'def metodo() print("metodo") end',
        'def metodo print ("es metodo?") end',
        'print "Hola mundo"',
        'put "hola mundo"']


    resultado = ''
    def __init__(self):

        self.raiz = Tk()
        self.raiz.title("Validar Ruby")
        fuente = font.Font(weight='bold')

        self.help = messagebox

        frame_entry = Frame(self.raiz)
        frame_result = Frame(self.raiz)
        frame_top = Frame(frame_entry)

                              
        self.etiq1 = ttk.Label(frame_entry, text="Validar expresión:", 
                               font=fuente)
        self.etiq2 = ttk.Label(frame_result, text="Resultado:", 
                               font=fuente)
        
        
        self.usuario = StringVar()
        self.clave = StringVar()
        self.ctext1 = Text(frame_entry, bg='black',fg='#B0F638', 
                                width=50, height=20)
        
        self.ctext2 = Text(frame_result,  
                                width=50, height=20)
        self.separ1 = ttk.Separator(self.raiz, orient=VERTICAL)
        
        frame_botons = Frame(self.raiz)
        self.boton1 = ttk.Button(frame_botons, text="Aceptar", 
                                 command=self.aceptar)
        self.boton2 = ttk.Button(frame_botons,text="Cancelar", 
                                 command=quit)
        self.boton3 = ttk.Button(frame_botons, text="Algoritmo aleatorio", 
                                 command=self.algoritmo)

        self.boton4 = ttk.Button(frame_top, text="Agregar código de prueba", 
                                 command=self.insertar)  

        self.boton5 = ttk.Button(frame_top, text="¿Cómo funciona?", 
                                 command=self.alert_help)                     
                                 
        self.ctext1.insert("end",">> ")
        frame_botons.pack(side = BOTTOM, fill=BOTH, expand=False, padx=5, pady=5)                       
        frame_result.pack(side = RIGHT, fill=BOTH, expand=True, padx=70, pady=70)                       
        frame_entry.pack(side = LEFT, fill=BOTH, expand=True, padx=70, pady=70)                       
                               

        self.boton4.pack(side=LEFT, expand=True, 
                         padx=1, pady=1)
        self.boton5.pack(side=RIGHT, expand=True, 
                         padx=1, pady=1)
        self.etiq1.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=5, pady=5)
        frame_top.pack(side = TOP, fill=BOTH, expand=True, padx=10, pady=10)
        
        self.ctext1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=30)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True, 
                        padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=30)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        self.boton3.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=5, pady=5)
        
        
    
        self.ctext2.focus_set()
        
        self.raiz.mainloop()
    

    
    def aceptar(self):
        entrada = self.ctext1.get(1.0,"end").split(">>")
        self.ctext2.delete(1.0,"end")
        for i in entrada:
            if(i!=""):
                print(i)
                result = parser.parse(i)
                global resultado
                self.ctext2.insert("end","\n" + str(resultado))# aqui se pone el valor de resultado en la caja de texto
           
            
    
    def algoritmo(self):
        num= random.randint(0, len(self.array_randoms)-1)
        self.ctext1.insert("end","\n>> "+ self.array_randoms[num])
        result = parser.parse(self.array_randoms[num])
        self.ctext2.insert("end","\n" + resultado)

    def insertar(self):
        self.ctext1.insert("end","\n>> ")

    #instrucciones a usarse en la GUI para mejor entendimiento del codigo
    def alert_help(self):
        self.help.showinfo("¿Cómo funciona?","Las instrucciones empiezan desde '>>' y se tomará cada línea como parte de la instrucción. Para agregar otra instrucción presione el botón 'Agregar código de prueba'. Puede presionar el botón 'Algoritmo aleatorio' para agregar instrucciones aleatorias. Presione 'Aceptar' para ver el resultado.")

# >> if 3>2 then
# puts("h")
# end
# >> true and true
# >>8+8

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()

#End Hector Rizzo


