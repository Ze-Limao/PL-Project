import sys 
from translator import Translator
from analisadorlexico import Lexer
from analisadorsintatico import Parser


# Versão analisador lexico
#def main(args):
#    lexer = analisadorlexico.Lexer()
#    translation = Translator()
#
#    with open(args[1], 'r') as file:
#        lines = file.readlines()
#    for line in lines:
#        data = line.strip()
#        lexer.input(data)
#        for i in lexer.lexer:
#            if i.type == 'STRING':
#                value = translation.forth_push(i.value)
#                print(value)
#            if i.type == 'NUMBER':
#                value = translation.forth_push(i.value)
#                print(value)
#            elif i.type == 'MATH_OPERATOR':
#                value = translation.forth_math(i.value)
#                print(value)
#            elif i.type == 'POP':
#                value = translation.forth_pop()
#                print(value)
#            elif i.type == 'DOT':
#                value = translation.forth_print()
#                print(value)
#            elif i.type == 'COLON':
#                in_func = True
#                print("A iniciar função")
#        
#    print(translation.code)
            
def main(args):
    lexer = Lexer()
    translator = Translator()
    parser = Parser(lexer, translator)
    while True:
        try:
            s = input('calc >> ')
        except EOFError or KeyboardInterrupt:
            break
        if not s: 
            continue
        result = parser.parse(s)
        if result:
            print(result)
    
    print(translator.code)
    translator.code_to_file()


if __name__ == '__main__':
    main(args=sys.argv)