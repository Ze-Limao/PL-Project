class Translator:
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.functions = []
        self.loops = []
        self.function_names = []
        self.code = []
        self.code.append("start")
        self.code.append("")
        self.var_counter = 0
        self.ifcounter = 0
        self.func_count = -1
        self.loop_count = -1
    
    def nop(self):
        self.code.append("nop") # Nope operation does nothing
        return None
    
    def error(self, message):
        self.code.append(f"error {message}")
        return message

    def push(self, value, in_func : bool, in_loop : bool):
        self.stack.append(value)
        if type(value) == str:
            if in_func and not in_loop:
                self.functions[self.func_count].append(f"pushs \"{value}\"")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append(f"pushs \"{value}\"")
            elif not in_func and not in_loop:
                self.code.append(f"pushs \"{value}\"")
        if type(value) == int:
            if in_func and not in_loop:
                self.functions[self.func_count].append(f"pushi {value}")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append(f"pushi {value}")
            elif not in_func and not in_loop:
                self.code.append(f"pushi {value}")
        if type(value) == float:
            if in_func and not in_loop:
                self.functions[self.func_count].append(f"pushf {value}")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append(f"pushf {value}")
            elif not in_func and not in_loop:
                self.code.append(f"pushf {value}")
        return value
    
    def pop(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append("pop")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append("pop")
        elif not in_func and not in_loop: 
            self.code.append("pop")

    def dup(self, in_func : bool, in_loop : bool):
        value = self.stack[-1]
        self.stack.append(value)
        if in_func and not in_loop:
            self.functions[self.func_count].append("dup 1")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append("dup 1")
        elif not in_func and not in_loop:
            self.code.append("dup 1")
        return value

    def swap(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append("swap")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append("swap")
        elif not in_func and not in_loop:
            self.code.append("swap")
        #return a, b
    
    def math(self, operator, in_func : bool, in_loop : bool):
        b = self.stack.pop()
        a = self.stack.pop()
        if operator == "+":
            result = a + b
            if in_func and not in_loop:
                self.functions[self.func_count].append("add")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("add")
            elif not in_func and not in_loop:
                self.code.append("add")
        elif operator == "-":
            result = a - b
            if in_func and not in_loop:
                self.functions[self.func_count].append("sub")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("sub")
            elif not in_func and not in_loop:
                self.code.append("sub")
        elif operator == "*":
            result = a * b
            if in_func and not in_loop:
                self.functions[self.func_count].append("mul")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("mul")
            elif not in_func and not in_loop:
                self.code.append("mul")
        elif operator == "/":
            result = a / b
            if in_func and not in_loop:
                self.functions[self.func_count].append("div")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("div")
            elif not in_func and not in_loop:
                self.code.append("div")
        elif operator == "=":
            result = a == b
            if in_func and not in_loop:
                self.functions[self.func_count].append("equal")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("equal")
            elif not in_func and not in_loop:
                self.code.append("equal")
        elif operator == "%":
            result = a % b
            if in_func and not in_loop:
                self.functions[self.func_count].append("mod")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("mod")
            elif not in_func and not in_loop:
                self.code.append("mod")
        elif operator == "<":
            result = a < b
            if in_func and not in_loop:
                self.functions[self.func_count].append("inf")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("inf")
            elif not in_func and not in_loop:
                self.code.append("inf")
        elif operator == "<=":
            result = a <= b
            if in_func and not in_loop:
                self.functions[self.func_count].append("infeq")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("infeq")
            elif not in_func and not in_loop:
                self.code.append("infeq")
        elif operator == ">":
            result = a > b
            if in_func and not in_loop:
                self.functions[self.func_count].append("sup")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("sup")
            elif not in_func and not in_loop:
                self.code.append("sup")
        elif operator == ">=":
            result = a >= b
            if in_func and not in_loop:
                self.functions[self.func_count].append("supeq")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("supeq")
            elif not in_func and not in_loop:
                self.code.append("supeq")
        else:
            raise ValueError("Invalid operator")
        self.stack.append(result)
        return result


    def print(self, in_func : bool, in_loop : bool):
        result = self.stack.pop()
        if isinstance(result, str):
            if in_func and not in_loop:
                self.functions[self.func_count].append("writes")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("writes")
            elif not in_func and not in_loop:
                self.code.append(f"writes")
        elif result == int(result):
            if in_func and not in_loop:
                self.functions[self.func_count].append("writei")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("writei")
            elif not in_func and not in_loop:
                self.code.append(f"writei") # EMIT

        else:
            if in_func and not in_loop:
                self.functions[self.func_count].append("writef")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append("writef")
            elif not in_func and not in_loop:
                self.code.append(f"writef")
        return result
    
    def char(self, value):
        result = ord(value)
        self.push(result)
    
    def input_key(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append("read")
            self.functions[self.func_count].append("atoi")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append("read")
            self.loops[self.loop_count].append("atoi")
        elif not in_func and not in_loop:
            self.code.append("read")
            self.code.append("atoi")
        return None
    
    def print_string(self, value, in_func : bool, in_loop : bool):
        value = value[3:-1]
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"pushs \"{value}\"")
            self.functions[self.func_count].append("writes")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"pushs \"{value}\"")
            self.loops[self.loop_count].append("writes")
        elif not in_func and not in_loop:
            self.code.append(f"pushs \"{value}\"")
            self.code.append("writes")
        return value

    def emit(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"writechr")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"writechr")
        elif not in_func and not in_loop:
            self.code.append(f"writechr") 

    def cr(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append("cr")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append("cr")
        elif not in_func and not in_loop:
            self.code.append("cr")

    def _if(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append("if")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append("if")
        elif not in_func and not in_loop:
            self.code.append("if")
        return self.stack.pop()
    
    def _else(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append("else")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append("else")
        elif not in_func and not in_loop:
            self.code.append("else")
        return self.stack.pop()
    
    def then(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append("then")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append("then")
        elif not in_func and not in_loop:
            self.code.append("then")
        return self.stack.pop()
    
    def load(self, name, arg, in_func : bool, in_loop : bool):
        self.stack.append(self.variables[name]) # Coloca as variaveis na stack
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"load {arg}")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"load {arg}")
        elif not in_func and not in_loop:
            self.code.append(f"load {arg}")
        return self.variables[name][arg]

# Conversions

    def atoi(self, value):
        self.stack.append(int(value))
        self.code.append("atoi")
        return int(value)
    
    def atof(self, value):
        self.stack.append(float(value))
        self.code.append("atof")
        return float(value)
    
    def itof(self, value):
        self.stack.append(float(value))
        self.code.append("itof")
        return float(value)
    
    def ftoi(self, value):
        self.stack.append(int(value))
        self.code.append("ftoi")
        return int(value)
    
    def stri(self, value):
        self.stack.append(int(value))
        self.code.append("stri")
        return int(value)
    
    def strf(self, value):
        self.stack.append(float(value))
        self.code.append("strf")
        return float(value)

# Variables
    def init_var(self, name, in_func : bool, in_loop : bool):
        if name not in self.variables:
            self.variables[name] = [self.var_counter, 0]  # index and value
            if in_func and not in_loop:
                self.functions[self.func_count].insert(0, f"pushi 0")
                self.functions[self.func_count].append(f"pushi 0")
                self.functions[self.func_count].append(f"storeg {self.variables[name][0]}")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].insert(0, f"pushi 0")
                self.loops[self.loop_count].append(f"pushi 0")
                self.loops[self.loop_count].append(f"storeg {self.variables[name][0]}")
            elif not in_func and not in_loop:
                self.code.insert(0, f"pushi 0")
                self.code.append(f"pushi 0")
                self.code.append(f"storeg {self.variables[name][0]}")
            self.var_counter += 1
            return name
        else:
            print(f"Variable {name} already exists")
            return None     

    def getset(self, name, value, in_func : bool, in_loop : bool):
        if name in self.variables:
            index = self.variables[name][0]
            if value == "!":  # Set
                if self.stack:
                    self.variables[name][1] = self.stack.pop()
                    if in_func and not in_loop:
                        self.functions[self.func_count].append(f"storeg {index}")
                    elif (in_loop and not in_func) or (in_func and in_loop):
                        self.loops[self.loop_count].append(f"storeg {index}")
                    elif not in_func and not in_loop:
                        self.code.append(f"storeg {index}")
                    return name, self.variables[name][1]
                else:
                    return None
            elif value == "@":  # Get
                self.stack.append(self.variables[name][1])
                if in_func and not in_loop:
                    self.functions[self.func_count].append(f"pushg {index}")
                elif (in_loop and not in_func) or (in_func and in_loop):
                    self.loops[self.loop_count].append(f"pushg {index}")
                elif not in_func and not in_loop:
                    self.code.append(f"pushg {index}")
                return self.variables[name][1]
        else:
            print(f"Variable {name} does not exist")
            return None

    def space(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"pushs " "")
            self.functions[self.func_count].append("writes")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"pushs " "")
            self.loops[self.loop_count].append("writes")
        elif not in_func and not in_loop:  
            self.code.append(f"pushs " "")
            self.code.append("writes")
        return None

    def spaces(self, in_func : bool, in_loop : bool):
        value = self.stack.pop()
        if isinstance(value, int):
            if in_func and not in_loop:
                self.functions[self.func_count].append(f"pop")
                self.functions[self.func_count].append(f"pushs {' ' * value}")
                self.functions[self.func_count].append("writes")
            elif (in_loop and not in_func) or (in_func and in_loop):
                self.loops[self.loop_count].append(f"pop")
                self.loops[self.loop_count].append(f"pushs {' ' * value}")
                self.loops[self.loop_count].append("writes")
            elif not in_func and not in_loop:
                self.code.append(f"pop")
                self.code.append(f"pushs {' ' * value}")
                self.code.append("writes")
            return ' ' * value
        else:
            return None

# Functions

    def init_func(self):
        func = []
        self.functions.append(func)
        self.func_count += 1

# Loops

    def init_loop(self):
        loop = []
        self.loops.append(loop)
        self.loop_count += 1

    def _while(self):
        self.loops[self.loop_count].append(f"jz endloop{self.loop_count+1}")
        
    def repeat(self):
        self.loops[self.loop_count].append(f"jump loop{self.loop_count+1}")
        self.loops[self.loop_count].append(f"endloop{self.loop_count+1}:")
        
    def until(self):
        self.loops[self.loop_count].append(f"jz loop{self.loop_count+1}")

# Control Operations

    def pusha(self, value, in_func : bool, in_loop : bool):
        self.stack.append(value)
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"pusha {value}")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"pusha {value}")
        elif not in_func and not in_loop:
            self.code.append(f"pusha {value}")
        return value
    
    def jump(self, label, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"jump {label}")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"jump {label}")
        elif not in_func and not in_loop:
            self.code.append(f"jump {label}")
        return label
    
    def jz(self, label, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"jz {label}")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"jz {label}")
        elif not in_func and not in_loop:
            self.code.append(f"jz {label}")
        return label
    
    def call(self, name, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"pusha {name}")
            self.functions[self.func_count].append(f"call")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"pusha {name}")
            self.loops[self.loop_count].append(f"call")
        elif not in_func and not in_loop:
            self.code.append(f"pusha {name}")
            self.code.append(f"call")
        return name

    def _return(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append("return")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append("return")
        elif not in_func and not in_loop:
            self.code.append("return")
        return self.stack.pop()
    

    def code_to_file(self):
        filename = "../outputs/output.txt"
        with open(filename, 'w') as file:
            for line in self.code:
                file.write(f"{line}\n")
            file.close()

    def function_to_file(self):
        filename = "../outputs/output.txt"
        with open(filename, 'a') as file:
            for line in self.code:
                file.write(f"{line}\n")
            file.write(f"return\n")
            file.close()
            
    def loop_to_file(self, loop_n : int):
        filename = "../outputs/output.txt"
        with open(filename, 'a') as file:
            for line in self.code:
                file.write(f"{line}\n")
            file.close()
            
# Conditionals

    def if_then(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"jz else{self.ifcounter+1}")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"jz else{self.ifcounter+1}")
        elif not in_func and not in_loop:
            self.code.append(f"jz else{self.ifcounter+1}")

    def else_then(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"jump then{self.ifcounter+1}")
            self.functions[self.func_count].append(f"else{self.ifcounter+1}:")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"jump then{self.ifcounter+1}")
            self.loops[self.loop_count].append(f"else{self.ifcounter+1}:")
        elif not in_func and not in_loop:
            self.code.append(f"jump then{self.ifcounter+1}")
            self.code.append(f"else{self.ifcounter+1}:")

    def only_else_then(self, in_func : bool, in_loop : bool):
        if in_func and not in_loop:
            self.functions[self.func_count].append(f"then{self.ifcounter+1}:")
        elif (in_loop and not in_func) or (in_func and in_loop):
            self.loops[self.loop_count].append(f"then{self.ifcounter+1}:")
        elif not in_func and not in_loop:
            self.code.append(f"then{self.ifcounter+1}:")
        self.ifcounter += 1