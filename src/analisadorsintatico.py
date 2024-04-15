import sys
from ply import yacc
from analisadorlexico import tokens, lexer


class Parser:
    def __init__(self):
        self.parser = yacc()

    def build(self):
        self.parser.parse(lexer=lexer)

    def test(self, data):
        return self.parser.parse(data)

parser = yacc()
parser.exito = True

def p_expression(p):
    '''
    expression : NUMBER
                | STRING
                | expression expression MATH_OPERATOR
                | expression DOT
                | expression IF expression THEN expression ELSE expression
                | function
                |
    '''

def p_math_operator(p):
    '''
    MATH_OPERATOR : PLUS
                    | MINUS
                    | TIMES
                    | DIVIDE
                    | MOD
                    | LESS
                    | GREATER
                    | EQUAL
    '''
    p[0] = ('math_operator', p[1])


def p_function(p):
    '''
    function : COLON NAME LPAREN ARGUMENTS ARGDELIMITER ARGUMENT RPAREN expression SEMICOLON
    '''
    p[0] = ('function', p[2], p[3], p[5])


def p_arguments(p):
    '''
    arguments : ARGUMENT
              | arguments ARGUMENT
              |
    '''
    if len(p) == 2:
        p[0] = ('arguments', p[1])
    elif len(p) == 3:
        p[0] = ('arguments', p[1], p[2])


def p_error(p):
    print("Erro Sintático")
    parser.exito = False
