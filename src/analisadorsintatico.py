import sys
import ply.yacc as yacc
from analisadorlexico import Lexer, tokens
from translator import Translator


class Parser:
    def __init__(self):
        self.translator = Translator()
        self.lexer = Lexer()
        self.parser = yacc.yacc()
        self.parser.exito = True

    def run(self, filename):
        print("Analisando o arquivo:", filename)
        try:
            with open(filename, 'r') as file:
                for line in file:
                    result = self.parser.parse(line)
                    if self.parser.exito:
                        self.translator.code_to_file()
                        print("Análise bem-sucedida!")
                    else:
                        print("Erro na análise sintática.")
        except FileNotFoundError:
            print("Arquivo não encontrado:", filename)
        except Exception as e:
            print("Ocorreu um erro durante a análise:", e)
    
    def test(self):
        for line in sys.stdin: # isto é provisório
            result = self.parser.parse(line)
            if(self.parser.exito):
                print("correu bem")
'''

Program : Expression
        |

Expression : NUMBER
           | STRING
           | Expression Expression MATH_OPERATOR
           | Expression DOT
           | Expression IF Expression THEN Expression ELSE Expression
           | Function
           |

Function : COLON NAME LPAREN Arguments ARGDELIMITER ARGUMENT RPAREN Expression SEMICOLON

Arguments : ARGUMENT
          | Arguments ARGUMENT
          |  

'''
    
def p_expression(p):
    '''
    Expression : NUMBER
                | STRING
                | Expression Expression MATH_OPERATOR
                | Expression DOT
                | Expression IF Expression THEN Expression ELSE Expression
                | function
                |
    '''


def p_function(p):
    '''
    function : COLON NAME LPAREN Arguments ARGDELIMITER ARGUMENT RPAREN Expression SEMICOLON
    '''
    p[0] = ('function', p[2], p[3], p[5])


def p_arguments(p):
    '''
    Arguments : ARGUMENT
              | Arguments ARGUMENT
              |
    '''
    if len(p) == 2:
        p[0] = ('arguments', p[1])
    elif len(p) == 3:
        p[0] = ('arguments', p[1], p[2])


def p_error(p):
    print("Erro Sintático")
    Parser.parser.exito = False


def main(args):
    file = args[1]
    parser = Parser()
    parser.test()

if __name__ == '__main__':
    main(args=sys.argv)