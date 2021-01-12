
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "left=ADDASSIGNSUBASSIGNMULASSIGNDIVASSIGNleftLTGTNGTNLTNEQEQleft+-DOTADDDOTSUBleft*/DOTMULDOTDIVnonassocONESZEROSEYEnonassocTRANSPOSITIONnonassocIFXnonassocELSErightOPPADDASSIGN BREAK CONTINUE DIVASSIGN DOTADD DOTDIV DOTMUL DOTSUB ELSE EQ EYE FLOAT FOR GT ID IF INTNUM LT MULASSIGN NEQ NGT NLT ONES PRINT RETURN STRING SUBASSIGN TRANSPOSITION WHILE ZEROS\n    program : instruction\n     \n    program : program instruction\n    instruction : expression ';' \n    instruction : BREAK ';'\n     \n    instruction : CONTINUE ';'\n     \n    instruction : RETURN expression ';'\n    \n    instructions_list : instruction\n    \n    instructions_list : instructions_list instruction\n    \n    instruction : '{' instructions_list '}'\n    \n    expression : '(' expression ')'\n    \n    expression : '[' ']'\n    \n    expression : '[' expression_list ']'\n    \n    expression : INTNUM\n    \n    expression : FLOAT\n    \n    expression : ID\n    \n    expression : STRING\n    \n    expression : expression TRANSPOSITION\n    \n    expression : '-' expression %prec OPP\n    \n    expression : ZEROS '(' expression_list ')'\n               | ONES '(' expression_list ')'\n               | EYE '(' expression_list ')'\n    \n    expression : ID '=' expression       \n                 | ID ADDASSIGN expression\n                 | ID SUBASSIGN expression \n                 | ID MULASSIGN expression\n                 | ID DIVASSIGN expression\n    \n    expression : ID '[' expression_list ']' '=' expression       \n               | ID '[' expression_list ']' ADDASSIGN expression\n               | ID '[' expression_list ']' SUBASSIGN expression \n               | ID '[' expression_list ']' MULASSIGN expression\n               | ID '[' expression_list ']' DIVASSIGN expression\n    \n    expression : ID '[' expression_list ']'\n     \n    expression : expression '+' expression\n               | expression '-' expression\n               | expression '*' expression\n               | expression '/' expression\n               | expression DOTADD expression\n               | expression DOTSUB expression\n               | expression DOTMUL expression\n               | expression DOTDIV expression\n               | expression EQ expression\n               | expression NEQ expression\n               | expression LT expression\n               | expression NLT expression\n               | expression GT expression\n               | expression NGT expression\n    \n    expression_list : expression\n    \n    expression_list : expression_list ',' expression\n    \n    instruction : IF '(' expression ')' instruction ELSE instruction\n    \n    instruction : IF '(' expression ')' instruction %prec IFX\n    \n    instruction : WHILE '(' expression ')' instruction\n    \n    range : expression ':' expression\n    \n    instruction : FOR ID '=' range instruction\n    \n    instruction : PRINT expression_list ';'\n    "
    
_lr_action_items = {'BREAK':([0,1,2,7,12,15,16,17,22,23,24,39,40,42,43,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,83,84,85,86,87,89,91,95,96,97,99,101,102,103,104,105,106,113,114,115,116,117,118,119,120,],[4,4,-1,4,-15,-13,-14,-16,-2,-3,-17,-4,-5,4,-7,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,-22,-23,-24,-25,-26,-54,-12,4,4,4,-32,-19,-20,-21,-50,-51,-53,4,-52,-27,-28,-29,-30,-31,-49,]),'CONTINUE':([0,1,2,7,12,15,16,17,22,23,24,39,40,42,43,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,83,84,85,86,87,89,91,95,96,97,99,101,102,103,104,105,106,113,114,115,116,117,118,119,120,],[5,5,-1,5,-15,-13,-14,-16,-2,-3,-17,-4,-5,5,-7,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,-22,-23,-24,-25,-26,-54,-12,5,5,5,-32,-19,-20,-21,-50,-51,-53,5,-52,-27,-28,-29,-30,-31,-49,]),'RETURN':([0,1,2,7,12,15,16,17,22,23,24,39,40,42,43,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,83,84,85,86,87,89,91,95,96,97,99,101,102,103,104,105,106,113,114,115,116,117,118,119,120,],[6,6,-1,6,-15,-13,-14,-16,-2,-3,-17,-4,-5,6,-7,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,-22,-23,-24,-25,-26,-54,-12,6,6,6,-32,-19,-20,-21,-50,-51,-53,6,-52,-27,-28,-29,-30,-31,-49,]),'{':([0,1,2,7,12,15,16,17,22,23,24,39,40,42,43,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,83,84,85,86,87,89,91,95,96,97,99,101,102,103,104,105,106,113,114,115,116,117,118,119,120,],[7,7,-1,7,-15,-13,-14,-16,-2,-3,-17,-4,-5,7,-7,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,-22,-23,-24,-25,-26,-54,-12,7,7,7,-32,-19,-20,-21,-50,-51,-53,7,-52,-27,-28,-29,-30,-31,-49,]),'IF':([0,1,2,7,12,15,16,17,22,23,24,39,40,42,43,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,83,84,85,86,87,89,91,95,96,97,99,101,102,103,104,105,106,113,114,115,116,117,118,119,120,],[8,8,-1,8,-15,-13,-14,-16,-2,-3,-17,-4,-5,8,-7,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,-22,-23,-24,-25,-26,-54,-12,8,8,8,-32,-19,-20,-21,-50,-51,-53,8,-52,-27,-28,-29,-30,-31,-49,]),'WHILE':([0,1,2,7,12,15,16,17,22,23,24,39,40,42,43,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,83,84,85,86,87,89,91,95,96,97,99,101,102,103,104,105,106,113,114,115,116,117,118,119,120,],[10,10,-1,10,-15,-13,-14,-16,-2,-3,-17,-4,-5,10,-7,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,-22,-23,-24,-25,-26,-54,-12,10,10,10,-32,-19,-20,-21,-50,-51,-53,10,-52,-27,-28,-29,-30,-31,-49,]),'FOR':([0,1,2,7,12,15,16,17,22,23,24,39,40,42,43,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,83,84,85,86,87,89,91,95,96,97,99,101,102,103,104,105,106,113,114,115,116,117,118,119,120,],[11,11,-1,11,-15,-13,-14,-16,-2,-3,-17,-4,-5,11,-7,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,-22,-23,-24,-25,-26,-54,-12,11,11,11,-32,-19,-20,-21,-50,-51,-53,11,-52,-27,-28,-29,-30,-31,-49,]),'PRINT':([0,1,2,7,12,15,16,17,22,23,24,39,40,42,43,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,83,84,85,86,87,89,91,95,96,97,99,101,102,103,104,105,106,113,114,115,116,117,118,119,120,],[13,13,-1,13,-15,-13,-14,-16,-2,-3,-17,-4,-5,13,-7,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,-22,-23,-24,-25,-26,-54,-12,13,13,13,-32,-19,-20,-21,-50,-51,-53,13,-52,-27,-28,-29,-30,-31,-49,]),'(':([0,1,2,6,7,8,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,48,49,50,51,52,53,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,89,90,91,95,96,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[9,9,-1,9,9,44,9,46,-15,9,9,-13,-14,-16,9,59,60,61,-2,-3,-17,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-4,-5,9,-7,9,9,9,9,9,9,9,9,-11,-18,9,9,9,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,9,-22,-23,-24,-25,-26,-54,9,-12,9,9,9,-32,-19,-20,-21,-50,-51,-53,9,9,9,9,9,9,9,-52,-27,-28,-29,-30,-31,-49,]),'[':([0,1,2,6,7,9,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,48,49,50,51,52,53,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,89,90,91,95,96,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[14,14,-1,14,14,14,53,14,14,-13,-14,-16,14,-2,-3,-17,14,14,14,14,14,14,14,14,14,14,14,14,14,14,-4,-5,14,-7,14,14,14,14,14,14,14,14,-11,-18,14,14,14,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,14,-22,-23,-24,-25,-26,-54,14,-12,14,14,14,-32,-19,-20,-21,-50,-51,-53,14,14,14,14,14,14,14,-52,-27,-28,-29,-30,-31,-49,]),'INTNUM':([0,1,2,6,7,9,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,48,49,50,51,52,53,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,89,90,91,95,96,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[15,15,-1,15,15,15,-15,15,15,-13,-14,-16,15,-2,-3,-17,15,15,15,15,15,15,15,15,15,15,15,15,15,15,-4,-5,15,-7,15,15,15,15,15,15,15,15,-11,-18,15,15,15,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,15,-22,-23,-24,-25,-26,-54,15,-12,15,15,15,-32,-19,-20,-21,-50,-51,-53,15,15,15,15,15,15,15,-52,-27,-28,-29,-30,-31,-49,]),'FLOAT':([0,1,2,6,7,9,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,48,49,50,51,52,53,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,89,90,91,95,96,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[16,16,-1,16,16,16,-15,16,16,-13,-14,-16,16,-2,-3,-17,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-4,-5,16,-7,16,16,16,16,16,16,16,16,-11,-18,16,16,16,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,16,-22,-23,-24,-25,-26,-54,16,-12,16,16,16,-32,-19,-20,-21,-50,-51,-53,16,16,16,16,16,16,16,-52,-27,-28,-29,-30,-31,-49,]),'ID':([0,1,2,6,7,9,11,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,48,49,50,51,52,53,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,89,90,91,95,96,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[12,12,-1,12,12,12,47,-15,12,12,-13,-14,-16,12,-2,-3,-17,12,12,12,12,12,12,12,12,12,12,12,12,12,12,-4,-5,12,-7,12,12,12,12,12,12,12,12,-11,-18,12,12,12,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,12,-22,-23,-24,-25,-26,-54,12,-12,12,12,12,-32,-19,-20,-21,-50,-51,-53,12,12,12,12,12,12,12,-52,-27,-28,-29,-30,-31,-49,]),'STRING':([0,1,2,6,7,9,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,48,49,50,51,52,53,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,89,90,91,95,96,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[17,17,-1,17,17,17,-15,17,17,-13,-14,-16,17,-2,-3,-17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-4,-5,17,-7,17,17,17,17,17,17,17,17,-11,-18,17,17,17,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,17,-22,-23,-24,-25,-26,-54,17,-12,17,17,17,-32,-19,-20,-21,-50,-51,-53,17,17,17,17,17,17,17,-52,-27,-28,-29,-30,-31,-49,]),'-':([0,1,2,3,6,7,9,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,48,49,50,51,52,53,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[18,18,-1,26,18,18,18,-15,18,18,-13,-14,-16,18,-2,-3,-17,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-4,-5,26,18,-7,18,26,18,18,18,18,18,18,18,26,-11,-18,18,18,18,-33,-34,-35,-36,-37,-38,-39,-40,26,26,26,26,26,26,-6,-9,-8,26,-10,26,18,26,26,26,26,26,-54,18,-12,18,18,18,26,-32,26,-19,-20,-21,-50,-51,-53,18,18,18,18,18,18,18,26,26,26,26,26,26,-49,]),'ZEROS':([0,1,2,6,7,9,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,48,49,50,51,52,53,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,89,90,91,95,96,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[19,19,-1,19,19,19,-15,19,19,-13,-14,-16,19,-2,-3,-17,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-4,-5,19,-7,19,19,19,19,19,19,19,19,-11,-18,19,19,19,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,19,-22,-23,-24,-25,-26,-54,19,-12,19,19,19,-32,-19,-20,-21,-50,-51,-53,19,19,19,19,19,19,19,-52,-27,-28,-29,-30,-31,-49,]),'ONES':([0,1,2,6,7,9,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,48,49,50,51,52,53,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,89,90,91,95,96,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[20,20,-1,20,20,20,-15,20,20,-13,-14,-16,20,-2,-3,-17,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-4,-5,20,-7,20,20,20,20,20,20,20,20,-11,-18,20,20,20,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,20,-22,-23,-24,-25,-26,-54,20,-12,20,20,20,-32,-19,-20,-21,-50,-51,-53,20,20,20,20,20,20,20,-52,-27,-28,-29,-30,-31,-49,]),'EYE':([0,1,2,6,7,9,12,13,14,15,16,17,18,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,46,48,49,50,51,52,53,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,84,85,86,87,89,90,91,95,96,97,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,],[21,21,-1,21,21,21,-15,21,21,-13,-14,-16,21,-2,-3,-17,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-4,-5,21,-7,21,21,21,21,21,21,21,21,-11,-18,21,21,21,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-6,-9,-8,-10,21,-22,-23,-24,-25,-26,-54,21,-12,21,21,21,-32,-19,-20,-21,-50,-51,-53,21,21,21,21,21,21,21,-52,-27,-28,-29,-30,-31,-49,]),'$end':([1,2,22,23,39,40,76,77,89,104,105,106,120,],[0,-1,-2,-3,-4,-5,-6,-9,-54,-50,-51,-53,-49,]),';':([3,4,5,12,15,16,17,24,41,54,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,80,83,84,85,86,87,91,99,100,101,102,103,115,116,117,118,119,],[23,39,40,-15,-13,-14,-16,-17,76,89,-47,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-10,-22,-23,-24,-25,-26,-12,-32,-48,-19,-20,-21,-27,-28,-29,-30,-31,]),'TRANSPOSITION':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[24,-15,-13,-14,-16,-17,24,24,24,-11,-18,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-10,24,24,24,24,24,24,-12,24,-32,24,-19,-20,-21,24,24,24,24,24,24,]),'+':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[25,-15,-13,-14,-16,-17,25,25,25,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,25,25,25,25,25,25,25,-10,25,25,25,25,25,25,-12,25,-32,25,-19,-20,-21,25,25,25,25,25,25,]),'*':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[27,-15,-13,-14,-16,-17,27,27,27,-11,-18,27,27,-35,-36,27,27,-39,-40,27,27,27,27,27,27,27,-10,27,27,27,27,27,27,-12,27,-32,27,-19,-20,-21,27,27,27,27,27,27,]),'/':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[28,-15,-13,-14,-16,-17,28,28,28,-11,-18,28,28,-35,-36,28,28,-39,-40,28,28,28,28,28,28,28,-10,28,28,28,28,28,28,-12,28,-32,28,-19,-20,-21,28,28,28,28,28,28,]),'DOTADD':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[29,-15,-13,-14,-16,-17,29,29,29,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,29,29,29,29,29,29,29,-10,29,29,29,29,29,29,-12,29,-32,29,-19,-20,-21,29,29,29,29,29,29,]),'DOTSUB':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[30,-15,-13,-14,-16,-17,30,30,30,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,30,30,30,30,30,30,30,-10,30,30,30,30,30,30,-12,30,-32,30,-19,-20,-21,30,30,30,30,30,30,]),'DOTMUL':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[31,-15,-13,-14,-16,-17,31,31,31,-11,-18,31,31,-35,-36,31,31,-39,-40,31,31,31,31,31,31,31,-10,31,31,31,31,31,31,-12,31,-32,31,-19,-20,-21,31,31,31,31,31,31,]),'DOTDIV':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[32,-15,-13,-14,-16,-17,32,32,32,-11,-18,32,32,-35,-36,32,32,-39,-40,32,32,32,32,32,32,32,-10,32,32,32,32,32,32,-12,32,-32,32,-19,-20,-21,32,32,32,32,32,32,]),'EQ':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[33,-15,-13,-14,-16,-17,33,33,33,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,33,-10,33,33,33,33,33,33,-12,33,-32,33,-19,-20,-21,33,33,33,33,33,33,]),'NEQ':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[34,-15,-13,-14,-16,-17,34,34,34,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,34,-10,34,34,34,34,34,34,-12,34,-32,34,-19,-20,-21,34,34,34,34,34,34,]),'LT':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[35,-15,-13,-14,-16,-17,35,35,35,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,35,-10,35,35,35,35,35,35,-12,35,-32,35,-19,-20,-21,35,35,35,35,35,35,]),'NLT':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[36,-15,-13,-14,-16,-17,36,36,36,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,36,-10,36,36,36,36,36,36,-12,36,-32,36,-19,-20,-21,36,36,36,36,36,36,]),'GT':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[37,-15,-13,-14,-16,-17,37,37,37,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,37,-10,37,37,37,37,37,37,-12,37,-32,37,-19,-20,-21,37,37,37,37,37,37,]),'NGT':([3,12,15,16,17,24,41,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,98,99,100,101,102,103,114,115,116,117,118,119,],[38,-15,-13,-14,-16,-17,38,38,38,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,38,-10,38,38,38,38,38,38,-12,38,-32,38,-19,-20,-21,38,38,38,38,38,38,]),')':([12,15,16,17,24,45,55,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,79,80,81,83,84,85,86,87,91,92,93,94,99,100,101,102,103,115,116,117,118,119,],[-15,-13,-14,-16,-17,80,-47,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,95,-10,96,-22,-23,-24,-25,-26,-12,101,102,103,-32,-48,-19,-20,-21,-27,-28,-29,-30,-31,]),',':([12,15,16,17,24,54,55,56,57,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,80,83,84,85,86,87,88,91,92,93,94,99,100,101,102,103,115,116,117,118,119,],[-15,-13,-14,-16,-17,90,-47,-11,90,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-10,-22,-23,-24,-25,-26,90,-12,90,90,90,-32,-48,-19,-20,-21,-27,-28,-29,-30,-31,]),']':([12,14,15,16,17,24,55,56,57,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,80,83,84,85,86,87,88,91,99,100,101,102,103,115,116,117,118,119,],[-15,56,-13,-14,-16,-17,-47,-11,91,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-10,-22,-23,-24,-25,-26,99,-12,-32,-48,-19,-20,-21,-27,-28,-29,-30,-31,]),':':([12,15,16,17,24,56,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,80,83,84,85,86,87,91,98,99,101,102,103,115,116,117,118,119,],[-15,-13,-14,-16,-17,-11,-18,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-10,-22,-23,-24,-25,-26,-12,107,-32,-19,-20,-21,-27,-28,-29,-30,-31,]),'=':([12,47,99,],[48,82,108,]),'ADDASSIGN':([12,99,],[49,109,]),'SUBASSIGN':([12,99,],[50,110,]),'MULASSIGN':([12,99,],[51,111,]),'DIVASSIGN':([12,99,],[52,112,]),'}':([23,39,40,42,43,76,77,78,89,104,105,106,120,],[-3,-4,-5,77,-7,-6,-9,-8,-54,-50,-51,-53,-49,]),'ELSE':([23,39,40,76,77,89,104,105,106,120,],[-3,-4,-5,-6,-9,-54,113,-51,-53,-49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'instruction':([0,1,7,42,95,96,97,113,],[2,22,43,78,104,105,106,120,]),'expression':([0,1,6,7,9,13,14,18,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,44,46,48,49,50,51,52,53,59,60,61,82,90,95,96,97,107,108,109,110,111,112,113,],[3,3,41,3,45,55,55,58,62,63,64,65,66,67,68,69,70,71,72,73,74,75,3,79,81,83,84,85,86,87,55,55,55,55,98,100,3,3,3,114,115,116,117,118,119,3,]),'instructions_list':([7,],[42,]),'expression_list':([13,14,53,59,60,61,],[54,57,88,92,93,94,]),'range':([82,],[97,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> instruction','program',1,'p_program','Mparser.py',33),
  ('program -> program instruction','program',2,'p_program_block','Mparser.py',39),
  ('instruction -> expression ;','instruction',2,'p_expression_instruction','Mparser.py',48),
  ('instruction -> BREAK ;','instruction',2,'p_break_instruction','Mparser.py',53),
  ('instruction -> CONTINUE ;','instruction',2,'p_continue_instruction','Mparser.py',59),
  ('instruction -> RETURN expression ;','instruction',3,'p_return_instruction','Mparser.py',65),
  ('instructions_list -> instruction','instructions_list',1,'p_instructions_list','Mparser.py',71),
  ('instructions_list -> instructions_list instruction','instructions_list',2,'p_instructions','Mparser.py',77),
  ('instruction -> { instructions_list }','instruction',3,'p_block_instruction','Mparser.py',85),
  ('expression -> ( expression )','expression',3,'p_expression_nest','Mparser.py',93),
  ('expression -> [ ]','expression',2,'p_expression_empty_vector','Mparser.py',99),
  ('expression -> [ expression_list ]','expression',3,'p_expression_vector','Mparser.py',105),
  ('expression -> INTNUM','expression',1,'p_expression_int','Mparser.py',111),
  ('expression -> FLOAT','expression',1,'p_expression_float','Mparser.py',117),
  ('expression -> ID','expression',1,'p_expression_id','Mparser.py',123),
  ('expression -> STRING','expression',1,'p_expression_string','Mparser.py',129),
  ('expression -> expression TRANSPOSITION','expression',2,'p_expression_transposition','Mparser.py',135),
  ('expression -> - expression','expression',2,'p_expression_opposite','Mparser.py',141),
  ('expression -> ZEROS ( expression_list )','expression',4,'p_expression_function','Mparser.py',147),
  ('expression -> ONES ( expression_list )','expression',4,'p_expression_function','Mparser.py',148),
  ('expression -> EYE ( expression_list )','expression',4,'p_expression_function','Mparser.py',149),
  ('expression -> ID = expression','expression',3,'p_expression_assign','Mparser.py',155),
  ('expression -> ID ADDASSIGN expression','expression',3,'p_expression_assign','Mparser.py',156),
  ('expression -> ID SUBASSIGN expression','expression',3,'p_expression_assign','Mparser.py',157),
  ('expression -> ID MULASSIGN expression','expression',3,'p_expression_assign','Mparser.py',158),
  ('expression -> ID DIVASSIGN expression','expression',3,'p_expression_assign','Mparser.py',159),
  ('expression -> ID [ expression_list ] = expression','expression',6,'p_expression_list_assign','Mparser.py',165),
  ('expression -> ID [ expression_list ] ADDASSIGN expression','expression',6,'p_expression_list_assign','Mparser.py',166),
  ('expression -> ID [ expression_list ] SUBASSIGN expression','expression',6,'p_expression_list_assign','Mparser.py',167),
  ('expression -> ID [ expression_list ] MULASSIGN expression','expression',6,'p_expression_list_assign','Mparser.py',168),
  ('expression -> ID [ expression_list ] DIVASSIGN expression','expression',6,'p_expression_list_assign','Mparser.py',169),
  ('expression -> ID [ expression_list ]','expression',4,'p_expression_array_reference','Mparser.py',176),
  ('expression -> expression + expression','expression',3,'p_expression_binary','Mparser.py',182),
  ('expression -> expression - expression','expression',3,'p_expression_binary','Mparser.py',183),
  ('expression -> expression * expression','expression',3,'p_expression_binary','Mparser.py',184),
  ('expression -> expression / expression','expression',3,'p_expression_binary','Mparser.py',185),
  ('expression -> expression DOTADD expression','expression',3,'p_expression_binary','Mparser.py',186),
  ('expression -> expression DOTSUB expression','expression',3,'p_expression_binary','Mparser.py',187),
  ('expression -> expression DOTMUL expression','expression',3,'p_expression_binary','Mparser.py',188),
  ('expression -> expression DOTDIV expression','expression',3,'p_expression_binary','Mparser.py',189),
  ('expression -> expression EQ expression','expression',3,'p_expression_binary','Mparser.py',190),
  ('expression -> expression NEQ expression','expression',3,'p_expression_binary','Mparser.py',191),
  ('expression -> expression LT expression','expression',3,'p_expression_binary','Mparser.py',192),
  ('expression -> expression NLT expression','expression',3,'p_expression_binary','Mparser.py',193),
  ('expression -> expression GT expression','expression',3,'p_expression_binary','Mparser.py',194),
  ('expression -> expression NGT expression','expression',3,'p_expression_binary','Mparser.py',195),
  ('expression_list -> expression','expression_list',1,'p_expression_list','Mparser.py',201),
  ('expression_list -> expression_list , expression','expression_list',3,'p_expressions','Mparser.py',207),
  ('instruction -> IF ( expression ) instruction ELSE instruction','instruction',7,'p_if_else_instruction','Mparser.py',217),
  ('instruction -> IF ( expression ) instruction','instruction',5,'p_if_instruction','Mparser.py',223),
  ('instruction -> WHILE ( expression ) instruction','instruction',5,'p_while_instruction','Mparser.py',229),
  ('range -> expression : expression','range',3,'p_range','Mparser.py',235),
  ('instruction -> FOR ID = range instruction','instruction',5,'p_for_instruction','Mparser.py',242),
  ('instruction -> PRINT expression_list ;','instruction',3,'p_print_instruction','Mparser.py',249),
]
