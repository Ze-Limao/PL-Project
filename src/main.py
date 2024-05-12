import sys 
from translator import Translator
from analisadorlexico import Lexer
from analisadorsintatico import Parser

def treat_data(data):
    treated_data = []
    buffer = ''
    for line in data:
        if '\\' in line:
            if buffer:
                treated_data.append(buffer)
                buffer = ''
        buffer += line.strip() + ' '
        if ';' in line or '\\' in line:
            treated_data.append(buffer)
            buffer = ''
    if buffer:
        treated_data.append(buffer)
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
            result = parser.parse(line)
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
    translator_code_aux = translator.code

    # Parte das funções
    if translator.functions:
        i = 0
        while i < len(translator.functions):
            function_name = translator.function_names[i]
            data = translator.functions[i]
            if ("pusha " + function_name) in translator_code_aux:
                translator.code = []
                translator.code.append(f"\n{function_name}:")
                for line in data:
                    translator.code.append(line)

                translator.function_to_file()
            i += 1

    # Parte dos loops
    if translator.loops:
        i = 0
        while i < len(translator.loops):
            data = translator.loops[i]
            translator.code = []
            translator.code.append("\nloop" + str(i+1) + ":")
            for line in data:
                translator.code.append(line)
            translator.loop_to_file(i+1)
            i += 1
            
    filename = "../outputs/output.txt"
    with open(filename, 'a') as file:
        file.write(f"stop\n")
        
if __name__ == '__main__':
    main(args=sys.argv)