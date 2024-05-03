import sys 
from translator import Translator
from analisadorlexico import Lexer
from analisadorsintatico import Parser

def main(args):
    i = 0
    lexer = Lexer()
    translator = Translator()
    parser = Parser(lexer, translator)
    if len(args) > 1:
        with open(args[1], 'r') as file:
            data = file.readlines()
        for line in data:
            result = parser.parse(line)
            print(i)
            i+=1
            if result:
                print(result)
    else:
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
    
    translator.code_to_file()

    # Parte das funções
    if translator.functions:
        print(translator.functions.keys())
        for key in translator.functions.keys():
                data = translator.functions[key]
                translator.code = []
                translator.code.append(f"\n{key}:")
                for line in data:
                    result2 = parser.parse(line)
                    print(i)
                    i+=1
                    if result2:
                        print(result2)
        
        translator.function_to_file()


if __name__ == '__main__':
    main(args=sys.argv)