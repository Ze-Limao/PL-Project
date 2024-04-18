
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARGDELIMITER ARGUMENT CHAR COLON COMMENT CR DOT ELSE EMIT FUNCTION_DEFINITION IF KEY LPAREN MATH_OPERATOR NAME NUMBER PRINTSTRING RPAREN SEMICOLON SPACE SPACES STRING THENExp : Exp NUMBERExp : Exp DOTExp : Exp MATH_OPERATOR\n        Exp : \n        '
    
_lr_action_items = {'NUMBER':([0,1,2,3,4,],[-4,2,-1,-2,-3,]),'DOT':([0,1,2,3,4,],[-4,3,-1,-2,-3,]),'MATH_OPERATOR':([0,1,2,3,4,],[-4,4,-1,-2,-3,]),'$end':([0,1,2,3,4,],[-4,0,-1,-2,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Exp':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Exp","S'",1,None,None,None),
  ('Exp -> Exp NUMBER','Exp',2,'p_number','analisadorsintatico.py',36),
  ('Exp -> Exp DOT','Exp',2,'p_dot','analisadorsintatico.py',42),
  ('Exp -> Exp MATH_OPERATOR','Exp',2,'p_math_operator','analisadorsintatico.py',48),
  ('Exp -> <empty>','Exp',0,'p_Empty','analisadorsintatico.py',54),
]
