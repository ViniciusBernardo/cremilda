
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'moduleCOMMA_ ELSE_ EQUAL_ FALSE IF_ LPAREN_ NAME NUMBER OP RPAREN_ SEMICOLON_ STRING THEN_ TK_SYMB_10_ TK_SYMB_9_ TRUE TYPENAMEatom : NUMBERatom : STRINGatom : TRUEatom : FALSEatom : TYPENAMEatom : NAMEatom : listdefargs : NAMEdefargs : NAME COMMA_ defargselem : valueelem : value OP valueelem : ifexprexpr : elemfargs : elemfargs : elem COMMA_ fargsfcall : value LPAREN_ RPAREN_fcall : value LPAREN_ fargs RPAREN_fundef : NAME LPAREN_ defargs RPAREN_ EQUAL_ exprifexpr : IF_ value THEN_ elem ELSE_ elemitems : elemitems : elem COMMA_ itemsitems : elem COMMA_ items COMMA_list : TK_SYMB_9_ TK_SYMB_10_list : TK_SYMB_9_ items TK_SYMB_10_module : statement SEMICOLON_module : statement SEMICOLON_ modulestatement : vardefstatement : fundefvalue : atomvalue : fcallvalue : LPAREN_ expr RPAREN_vardef : NAME EQUAL_ expr'
    
_lr_action_items = {'NAME':([0,6,7,8,17,18,25,28,29,35,42,44,46,48,53,],[5,5,10,26,10,10,10,10,10,26,10,10,10,10,10,]),'$end':([1,6,9,],[0,-25,-26,]),'SEMICOLON_':([2,3,4,10,11,12,13,14,15,16,19,20,21,22,23,24,32,37,38,41,43,47,51,55,],[6,-27,-28,-6,-32,-13,-10,-12,-29,-30,-1,-2,-3,-4,-5,-7,-23,-11,-16,-31,-24,-17,-18,-19,]),'EQUAL_':([5,36,],[7,46,]),'LPAREN_':([5,7,10,13,15,16,17,18,19,20,21,22,23,24,25,28,29,31,32,37,38,41,42,43,44,46,47,48,53,],[8,17,-6,29,-29,-30,17,17,-1,-2,-3,-4,-5,-7,17,17,17,29,-23,29,-16,-31,17,-24,17,17,-17,17,17,]),'IF_':([7,17,25,29,42,44,46,48,53,],[18,18,18,18,18,18,18,18,18,]),'NUMBER':([7,17,18,25,28,29,42,44,46,48,53,],[19,19,19,19,19,19,19,19,19,19,19,]),'STRING':([7,17,18,25,28,29,42,44,46,48,53,],[20,20,20,20,20,20,20,20,20,20,20,]),'TRUE':([7,17,18,25,28,29,42,44,46,48,53,],[21,21,21,21,21,21,21,21,21,21,21,]),'FALSE':([7,17,18,25,28,29,42,44,46,48,53,],[22,22,22,22,22,22,22,22,22,22,22,]),'TYPENAME':([7,17,18,25,28,29,42,44,46,48,53,],[23,23,23,23,23,23,23,23,23,23,23,]),'TK_SYMB_9_':([7,17,18,25,28,29,42,44,46,48,53,],[25,25,25,25,25,25,25,25,25,25,25,]),'OP':([10,13,15,16,19,20,21,22,23,24,32,38,41,43,47,],[-6,28,-29,-30,-1,-2,-3,-4,-5,-7,-23,-16,-31,-24,-17,]),'RPAREN_':([10,12,13,14,15,16,19,20,21,22,23,24,26,27,29,30,32,37,38,39,40,41,43,45,47,52,55,],[-6,-13,-10,-12,-29,-30,-1,-2,-3,-4,-5,-7,-8,36,38,41,-23,-11,-16,47,-14,-31,-24,-9,-17,-15,-19,]),'THEN_':([10,15,16,19,20,21,22,23,24,31,32,38,41,43,47,],[-6,-29,-30,-1,-2,-3,-4,-5,-7,42,-23,-16,-31,-24,-17,]),'COMMA_':([10,13,14,15,16,19,20,21,22,23,24,26,32,34,37,38,40,41,43,47,50,54,55,],[-6,-10,-12,-29,-30,-1,-2,-3,-4,-5,-7,35,-23,44,-11,-16,48,-31,-24,-17,54,-22,-19,]),'TK_SYMB_10_':([10,13,14,15,16,19,20,21,22,23,24,25,32,33,34,37,38,41,43,47,50,54,55,],[-6,-10,-12,-29,-30,-1,-2,-3,-4,-5,-7,32,-23,43,-20,-11,-16,-31,-24,-17,-21,-22,-19,]),'ELSE_':([10,13,14,15,16,19,20,21,22,23,24,32,37,38,41,43,47,49,55,],[-6,-10,-12,-29,-30,-1,-2,-3,-4,-5,-7,-23,-11,-16,-31,-24,-17,53,-19,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'module':([0,6,],[1,9,]),'statement':([0,6,],[2,2,]),'vardef':([0,6,],[3,3,]),'fundef':([0,6,],[4,4,]),'expr':([7,17,46,],[11,30,51,]),'elem':([7,17,25,29,42,44,46,48,53,],[12,12,34,40,49,34,12,40,55,]),'value':([7,17,18,25,28,29,42,44,46,48,53,],[13,13,31,13,37,13,13,13,13,13,13,]),'ifexpr':([7,17,25,29,42,44,46,48,53,],[14,14,14,14,14,14,14,14,14,]),'atom':([7,17,18,25,28,29,42,44,46,48,53,],[15,15,15,15,15,15,15,15,15,15,15,]),'fcall':([7,17,18,25,28,29,42,44,46,48,53,],[16,16,16,16,16,16,16,16,16,16,16,]),'list':([7,17,18,25,28,29,42,44,46,48,53,],[24,24,24,24,24,24,24,24,24,24,24,]),'defargs':([8,35,],[27,45,]),'items':([25,44,],[33,50,]),'fargs':([29,48,],[39,52,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> module","S'",1,None,None,None),
  ('atom -> NUMBER','atom',1,'p_atom_1','ply.py',126),
  ('atom -> STRING','atom',1,'p_atom_2','ply.py',126),
  ('atom -> TRUE','atom',1,'p_atom_3','ply.py',126),
  ('atom -> FALSE','atom',1,'p_atom_4','ply.py',126),
  ('atom -> TYPENAME','atom',1,'p_atom_5','ply.py',126),
  ('atom -> NAME','atom',1,'p_atom_6','ply.py',126),
  ('atom -> list','atom',1,'p_atom_7','ply.py',126),
  ('defargs -> NAME','defargs',1,'p_defargs_1','ply.py',126),
  ('defargs -> NAME COMMA_ defargs','defargs',3,'p_defargs_2','ply.py',126),
  ('elem -> value','elem',1,'p_elem_1','ply.py',126),
  ('elem -> value OP value','elem',3,'p_elem_2','ply.py',126),
  ('elem -> ifexpr','elem',1,'p_elem_3','ply.py',126),
  ('expr -> elem','expr',1,'p_expr_1','ply.py',126),
  ('fargs -> elem','fargs',1,'p_fargs_1','ply.py',126),
  ('fargs -> elem COMMA_ fargs','fargs',3,'p_fargs_2','ply.py',126),
  ('fcall -> value LPAREN_ RPAREN_','fcall',3,'p_fcall_1','ply.py',126),
  ('fcall -> value LPAREN_ fargs RPAREN_','fcall',4,'p_fcall_2','ply.py',126),
  ('fundef -> NAME LPAREN_ defargs RPAREN_ EQUAL_ expr','fundef',6,'p_fundef_1','ply.py',126),
  ('ifexpr -> IF_ value THEN_ elem ELSE_ elem','ifexpr',6,'p_ifexpr_1','ply.py',126),
  ('items -> elem','items',1,'p_items_1','ply.py',126),
  ('items -> elem COMMA_ items','items',3,'p_items_2','ply.py',126),
  ('items -> elem COMMA_ items COMMA_','items',4,'p_items_3','ply.py',126),
  ('list -> TK_SYMB_9_ TK_SYMB_10_','list',2,'p_list_1','ply.py',126),
  ('list -> TK_SYMB_9_ items TK_SYMB_10_','list',3,'p_list_2','ply.py',126),
  ('module -> statement SEMICOLON_','module',2,'p_module_1','ply.py',126),
  ('module -> statement SEMICOLON_ module','module',3,'p_module_2','ply.py',126),
  ('statement -> vardef','statement',1,'p_statement_1','ply.py',126),
  ('statement -> fundef','statement',1,'p_statement_2','ply.py',126),
  ('value -> atom','value',1,'p_value_1','ply.py',126),
  ('value -> fcall','value',1,'p_value_2','ply.py',126),
  ('value -> LPAREN_ expr RPAREN_','value',3,'p_value_3','ply.py',126),
  ('vardef -> NAME EQUAL_ expr','vardef',3,'p_vardef_1','ply.py',126),
]
