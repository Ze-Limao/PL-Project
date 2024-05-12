import sys 
from translator import Translator
from analisadorlexico import Lexer
from analisadorsintatico import Parser
import re

def treat_data(data):
    buffer = ''
    treated_data = []
    for line in data:
        if line.startswith(':'):
            if buffer:  # Append current buffer if it's not empty
                treated_data.append(buffer)
            buffer = line.strip() + ' '  # Start new buffer
        else:
            buffer += line.strip() + ' '
        if ';' in line:
            treated_data.append(buffer)
            buffer = ''
    if buffer:  # Append remaining buffer if it's not empty
        treated_data.append(buffer)
    print("Treated data")
    print(treated_data)
    print("End treated data")
    return treated_data

def main(args):
    i = 0
    lexer = Lexer()
    translator = Translator()
    parser = Parser(lexer, translator)
    if len(args) > 1:
        with open(args[1], 'r') as file:
            data = file.readlines()
        data = treat_data(data)
        for line in data:
            print(data)
            print(line)
            print("Ganda linha")
            result = parser.parse(line)
            print("Ganda linha")
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
    translator_code_aux = translator.code
    
    # Parte dos loops
    if translator.loops:
        print("Entrei nos loops FILHA DA PUTA")
        print(translator.loops)
        i = 0
        while i < len(translator.loops):
            data = translator.loops[i]
            print("-------------------")
            print(data)
            print("-------------------")
            translator.code = []
            translator.code.append("\nloop" + str(i+1) + ":")
            result2 = parser.parse(data)
            if result2:
                print(result2)
            print("Loop " + data)
            translator.function_to_file()
            print(translator.code)
            i += 1

    # Parte das funções
    if translator.functions:
        i = 0
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