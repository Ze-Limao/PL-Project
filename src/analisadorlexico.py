import sys 
from ply import lex

tokens_Function = [
    'NAME',
    'ARGUMENT',
    'RETURN',
    'IF',
    'ELSE',
    'THEN'
]

# Tokens Linguagem Forth
tokens = [
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'MOD',
    'LPAREN',
    'RPAREN',
    'COLON', # : Define inicio da função ou string  
    'SEMICOLON', # Finaliza função ou string 
    'DOT', # Print
    'LESS',
    'GREATER',
    'EQUAL',
    'EMIT',
    'KEY',
    'SPACE', #output a space
    'SPACES', #output n spaces
    'CHAR', #convert to ASCII
    'CR', #start new line , carriage return
]

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_SEMICOLON = r';'
t_DOT = r'\.'
t_COMMA = r','


def t_STRING(t):
    r'"[^"]*"'
    t.value = t.value[1:-1]  # Remove as aspas duplas
    return t

def t_NUMBER(t): 
    r"\d+(\.\d+)?"
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_MATH_OPERATOR(t):
    r"\+|-|\*|>|<|=|/|%"
    return t

def t_EMIT(t):
    r"[Ee][Mm][Ii][Tt]"
    return t

def t_KEY(t):
    r"[Kk][Ee][Yy]"
    return t

def t_SPACE(t):
    r"[Ss][Pp][Aa][Cc][Ee]"
    return t

def t_SPACES(t):
    r"[Ss][Pp][Aa][Cc][Ee][Ss]"
    return t

def t_CHAR(t):
    r"[Cc][Hh][Aa][Rr]"
    return t

def t_CR(t):
    r"[Cc][Rr]"
    return t

def t_NAME(t):
    r"[a-zA-Z_][a-zA-Z0-9_]*"
    return t

def t_COMMENT(t):
    #apanha tudo ate ao fim da linha a partir dos -- ou coisas entre parenteses
    r'\(.*\)|\b--.*|^--.*'
    t.lexer.lineno += t.value.count('\n')


def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)

def t_error(t):
    sys.stderr.write(f"Error: Unexpected character {t.value[0]}\n")
    t.lexer.skip(1) # Skip the character


t_DELIMITER = r","
t_FINAL_DELIMITER = r";"
t_ignore = " \t"  # Ignore spaces and tabs


def main (args):
    if len(args) < 2:
        return
    with open(args[1], 'r') as file:
        data = file.read()
        lexer = lex.lex() 
        lexer.input(data)
        for tok in lexer:
            print(tok) 

if __name__ == '__main__':
    main(args=sys.argv)