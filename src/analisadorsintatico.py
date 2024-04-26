import ply.yacc as yacc

class Parser():
    def __init__(self, lexer, translator):
      self.lexer = lexer
      self.tokens = self.lexer.tokens
      self.parser = yacc.yacc(module=self)
      self.translator = translator

    def parse(self, data):
        return self.parser.parse(data, lexer = self.lexer.lexer)

    '''
    Line : Line Exp
         | Line Function
         | Empty

    Exp : Cmd Exp
        | Cmd

    Cmd : NUMBER
        | MATH_OPERATION
        | Print
        | PRINTSTRING
        | CHAR CHR
        | CR
        | STRING
        | COMMENT
        | If Exp Else Exp EndOfIf
        | Loop
        | VARIABLE NAME
        | NAME Getset
        |

    Function : COLON NAME LPAREN Arguments ARGDELIMITER ARGUMENT RPAREN Cmd SEMICOLON

    Arguments : ARGUMENT
              | Arguments ARGUMENT
              | 

    Print : DOT
          | EMIT

    If : IF
    Else : ELSE Exp
         | 
    EndOfIf : THEN

    Getset : '!'
           | '@'
    
    '''

    def p_set(self, p):
        '''Cmd : Cmd NAME SET '''
        p[0] = p[1]
        self.translator.getset(p[2], p[3])

    def p_get(self, p):
        '''Cmd : Cmd NAME GET '''
        p[0] = p[1]
        self.translator.getset(p[2], p[3])

    def p_init_var(self, p):
        '''Cmd : Cmd VARIABLE NAME '''
        p[0] = p[1]
        self.translator.init_var(p[3])

    def p_cr(self, p):
        '''Cmd : Cmd CR'''
        p[0] = p[1]
        self.translator.cr()

    def p_string(self, p):
        '''Cmd : Cmd STRING'''
        p[0] = p[1]
        self.translator.push(p[2])

    def p_print2(self, p):
        '''Cmd : Cmd EMIT
        '''
        p[0] = p[1]    
        self.translator.emit()

    def p_print(self, p):
        '''Cmd : Cmd DOT
        '''
        p[0] = p[1]
        self.translator.print()
    
    def p_char(self, p):
        '''Cmd : Cmd CHR CHAR
               | Cmd CHR MATH_OPERATOR
        '''
        p[0] = p[1]
        self.translator.char(p[3])
    
    def p_dup(self,p):
        '''Cmd : Cmd DUP        
        '''
        p[0] = p[1]
        self.translator.dup()

    def p_printstring(self, p):
        '''Cmd : Cmd PRINTSTRING'''
        p[0] = p[1]
        self.translator.print_string(p[2])

    def p_number(self, p):
        '''Cmd : Cmd NUMBER'''
        p[0] = p[2]
        self.translator.push(p[2])
        
    def p_math_operator(self, p):
        '''Cmd : Cmd MATH_OPERATOR'''
        p[0] = p[2]
        self.translator.math(p[2])


    def p_cmdEmpty(self, p):
        '''Cmd : '''
        pass
    
    ## Function

    def p_function(self, p):
        '''
        Function : 
        '''
        return p
        

    def p_line(self, p):
        '''Line : Line Exp
                | Line Function
                | 
        '''
        return p

    def p_exp(self, p):
        '''Exp : Cmd Exp
               | Cmd
               |
        '''
        return p
    

    def p_error(self, p):
        print("Erro de sintaxe:", p)
        self.parse.parser.exito = False
