"""
    Frase : Frase Exp
          | Frase Func
          | 
          
    Exp : Comp 
        | Exp Comp

    Comp : NUM
         | Sinal
         | '.'
         | '.'TEXTO
         | CHAR CHR
         | EMIT
         | CR
         | DUP
         | KEY
         | SPACE
         | SPACES
         | ATOI
         | SWAP
         | If Exp StartOfELse Exp EnfOfIf
         | Loop
         | VARIABLE ID
         | ID WordExec

    Sinal: '+' ----------------------
         | '-'
         | '*'
         | '/'
         | '%'
         | 'OR'
         | 'AND'
         | '='

   WordExec: !     ---------------------
           | @    ------------
           |         --------------

   If : IF
   StartOfELse : ELSE Exp -----------------------------
               |           ----------------------------
   EnfOfIf : THEN

    Loop : Begin Exp EndOfLoopBegin
         | Do Exp EndOfLoopDo
    Begin : BEGIN
    EndOfLoopBegin : While Exp Repeat
                   | UNTIL
    While : WHILE
    Repeat : REPEAT

    Do : DO
    EndOfLoopDo : LOOP

    Func : FuncStart '(' Args MINUSMINUS PALAVRA ')' Definition
         | FuncStart Definition
    FuncStart : ':' ID
    Args : 
         | Args PALAVRA
    Definition : Exp ';'
"""
