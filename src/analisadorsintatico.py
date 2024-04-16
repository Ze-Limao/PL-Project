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
        '''Number : NUMBER'''
        p[0] = p[1]
        self.translator.forth_push(p[1])


    def p_error(self, p):
        print("Erro de sintaxe:", p)
        self.parse.parser.exito = False
