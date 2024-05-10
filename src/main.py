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
            print(data)
            print(line)
            result = parser.parse(line)
            print(i)
            i+=1
            if result:
                print(str(result) + " LOL")
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
        i = 0
        translator_code_aux = translator.code
        while i < len(translator.functions):
            print("CARALHO " + str(i))
            function_name = translator.function_names[i]
            data = translator.functions[i]
            if ("pusha " + function_name) in translator_code_aux:
                translator.code = []
                translator.code.append(f"\n{function_name}:")
                print(data + " blayeb")
                result2 = parser.parse(data)
                if result2:
                    print(result2)

                print("Function " + function_name)
                translator.function_to_file()
                print(translator.code)
            i += 1


if __name__ == '__main__':
    main(args=sys.argv)