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
    Expression : Number
               | STRING
               | COMMENT
               | Math_operation
               | Print
               | Expression IF Expression THEN Expression ELSE Expression
               | Function
               |

    Function : COLON NAME LPAREN Arguments ARGDELIMITER ARGUMENT RPAREN Expression SEMICOLON

    Arguments : ARGUMENT
              | Arguments ARGUMENT
              |  

    Math_operation : Number Number MATH_OPERATOR

    Print : DOT
    '''


    def p_number(self, p):
        '''Exp : Exp NUMBER'''
        p[0] = p[2]
        self.translator.forth_push(p[2])

    def p_dot(self, p):
        '''Exp : Exp DOT'''
        p[0] = p[1]
        self.translator.forth_print()
        
    def p_math_operator(self, p):
        '''Exp : Exp MATH_OPERATOR'''
        p[0] = p[2]
        self.translator.forth_math(p[2])
        
    def p_Empty(self,p):
        '''
        Exp : 
        '''


    def p_error(self, p):
        print("Erro de sintaxe:", p)
        self.parse.parser.exito = False
