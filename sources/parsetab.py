
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND BREAK CASE CLASS DEF DEFINED DIVIDE DO ELSE ELSIF END ENSURE EQUAL FALSE FOR GREATERTHAN GREATERTHANEQUAL IF IN LESSERTHAN LESSERTHANEQUAL LPAREN MINUS MOD MODULE NEXT NIL NOT NOTEQUAL NUMBER OR PLUS PUTS REDO RESCUE RETRY RETURN RPAREN SELF STRING SUPER SYMBOL TERM THEN TIMES TRUE UNDEF UNLESS UNTIL VAR_CLASS VAR_GLOBAL VAR_INSTANCE VAR_LOCAL VAR_SYSTEM WHEN WHILE YIELD _FILE_ _LINE_ beginsentence : print\n                | expression\n                | loopprint : VAR_GLOBALloop : WHILE expression do expression ENDdo : term\n        | DO\n\t\t| term DOterm : TERMexpression : expression PLUS termexpression : expression MINUS termexpression : termterm : term TIMES factorterm : term DIVIDE factorterm : factorfactor : NUMBERfactor : LPAREN expression RPAREN'
    
_lr_action_items = {'VAR_GLOBAL':([0,],[5,]),'WHILE':([0,],[7,]),'TERM':([0,6,7,8,9,10,11,12,13,16,18,19,20,21,22,23,24,25,27,],[8,-12,8,-9,-15,-16,8,8,8,8,-10,-11,-13,-14,8,-6,-7,-17,-8,]),'NUMBER':([0,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,27,],[10,-12,10,-9,-15,-16,10,10,10,10,10,10,-10,-11,-13,-14,10,-6,-7,-17,-8,]),'LPAREN':([0,6,7,8,9,10,11,12,13,14,15,16,18,19,20,21,22,23,24,25,27,],[11,-12,11,-9,-15,-16,11,11,11,11,11,11,-10,-11,-13,-14,11,-6,-7,-17,-8,]),'$end':([1,2,3,4,5,6,8,9,10,18,19,20,21,25,28,],[0,-1,-2,-3,-4,-12,-9,-15,-16,-10,-11,-13,-14,-17,-5,]),'PLUS':([3,6,8,9,10,16,17,18,19,20,21,25,26,],[12,-12,-9,-15,-16,12,12,-10,-11,-13,-14,-17,12,]),'MINUS':([3,6,8,9,10,16,17,18,19,20,21,25,26,],[13,-12,-9,-15,-16,13,13,-10,-11,-13,-14,-17,13,]),'DO':([6,8,9,10,16,18,19,20,21,23,25,],[-12,-9,-15,-16,24,-10,-11,-13,-14,27,-17,]),'RPAREN':([6,8,9,10,17,18,19,20,21,25,],[-12,-9,-15,-16,25,-10,-11,-13,-14,-17,]),'END':([6,8,9,10,18,19,20,21,25,26,],[-12,-9,-15,-16,-10,-11,-13,-14,-17,28,]),'TIMES':([6,8,9,10,18,19,20,21,23,25,],[14,-9,-15,-16,14,14,-13,-14,14,-17,]),'DIVIDE':([6,8,9,10,18,19,20,21,23,25,],[15,-9,-15,-16,15,15,-13,-14,15,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentence':([0,],[1,]),'print':([0,],[2,]),'expression':([0,7,11,22,],[3,16,17,26,]),'loop':([0,],[4,]),'term':([0,7,11,12,13,16,22,],[6,6,6,18,19,23,6,]),'factor':([0,7,11,12,13,14,15,16,22,],[9,9,9,9,9,20,21,9,9,]),'do':([16,],[22,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentence","S'",1,None,None,None),
  ('sentence -> print','sentence',1,'p_sentence','sintactico.py',9),
  ('sentence -> expression','sentence',1,'p_sentence','sintactico.py',10),
  ('sentence -> loop','sentence',1,'p_sentence','sintactico.py',11),
  ('print -> VAR_GLOBAL','print',1,'p_print','sintactico.py',14),
  ('loop -> WHILE expression do expression END','loop',5,'p_loop_while','sintactico.py',17),
  ('do -> term','do',1,'p_do','sintactico.py',20),
  ('do -> DO','do',1,'p_do','sintactico.py',21),
  ('do -> term DO','do',2,'p_do','sintactico.py',22),
  ('term -> TERM','term',1,'p_term','sintactico.py',24),
  ('expression -> expression PLUS term','expression',3,'p_expression_plus','sintactico.py',29),
  ('expression -> expression MINUS term','expression',3,'p_expression_minus','sintactico.py',33),
  ('expression -> term','expression',1,'p_expression_term','sintactico.py',37),
  ('term -> term TIMES factor','term',3,'p_term_times','sintactico.py',41),
  ('term -> term DIVIDE factor','term',3,'p_term_div','sintactico.py',45),
  ('term -> factor','term',1,'p_term_factor','sintactico.py',49),
  ('factor -> NUMBER','factor',1,'p_factor_num','sintactico.py',53),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor_expr','sintactico.py',57),
]
