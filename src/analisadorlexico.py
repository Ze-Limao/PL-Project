import sys
import ply.lex as lex

class Lexer():
    def __init__(self):
        self.lexer = lex.lex(module=self)

                    
    # Tokens Linguagem Forth
    tokens = [
        'NUMBER',
        'STRING',
        'LPAREN',
        'RPAREN',
        'COLON', # : Define inicio da função ou string  
        'SEMICOLON', # Finaliza função ou string 
        'DOT', # Print
        'EMIT',
        'KEY',
        'SPACE', #output a space
        'SPACES', #output n spaces
        'CHAR', #convert to ASCII
        'CR', #start new line , carriage return
        'NAME',
        'ARGUMENT',
        'IF',
        'ELSE',
        'THEN',
        'ARGDELIMITER',
        'COMMENT',
        'FUNCTION_DEFINITION',
        'MATH_OPERATOR',
        'PRINTSTRING'
    ]

    t_LPAREN = r'\('
    t_RPAREN = r'\)'
    t_COLON = r':'
    t_SEMICOLON = r';'
    t_DOT = r'\.'


    def t_PRINTSTRING(self, t):
        r'\."\s[^"]*"'
        t.value = t.value[2:-1]  # Remove as aspas duplas
        return t

    def t_STRING(self, t):
        r'"[^"]*"'
        t.value = t.value[1:-1]  # Remove as aspas duplas
        return t

    def t_NUMBER(self, t): 
        r"\d+(\.\d+)?"
        t.value = float(t.value) if '.' in t.value else int(t.value)
        return t

    def t_MATH_OPERATOR(self, t):
        r"\+|-|\*|>|<|=|/|%"
        return t

    def t_EMIT(self, t):
        r"[Ee][Mm][Ii][Tt]"
        return t

    def t_KEY(self, t):
        r"[Kk][Ee][Yy]"
        return t

    def t_SPACE(self, t):
        r"[Ss][Pp][Aa][Cc][Ee]"
        return t

    def t_SPACES(self, t):
        r"[Ss][Pp][Aa][Cc][Ee][Ss]"
        return t

    def t_CHAR(self, t):
        r"[Cc][Hh][Aa][Rr]"
        return t

    def t_CR(self, t):
        r"[Cc][Rr]"
        return t

    def t_NAME(self, t):
        r"[a-zA-Z_][a-zA-Z0-9_]*"
        return t


    def t_IF(self, t):
        r"[Ii][Ff]"
        return t

    def t_ELSE(self, t):
        r"[Ee][Ll][Ss][Ee]"
        return t

    def t_THEN(self, t):
        r"[Tt][Hh][Ee][Nn]"
        return t

    def t_ARGUMENT(self, t):
        r"[a-z][A-Z0-9]+"
        return t


    def t_COMMENT(self, t):
        # Apanha tudo ate ao fim da linha a partir dos -- ou coisas entre parenteses
        r'\(.*\)|\b--.*|^--.*'
        t.lexer.lineno += t.value.count('\n')

    def t_FUNCTION_DEFINITION(self, t):
        r': [a-zA-Z]+ ( . )* ;'
        return t

    def t_newline(self, t):
        r"\n+"
        t.lexer.lineno += len(self, t.value)

    def t_error(self, t):
        sys.stderr.write(f"Error: Unexpected character {t.value[0]}\n")
        t.lexer.skip(1) # Skip the character


    t_ignore = " \t\n"  # Ignore spaces and tabs