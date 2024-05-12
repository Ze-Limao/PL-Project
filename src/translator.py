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
        self.match_func_count = -1
        self.match_loop_count = -1
    
    def nop(self):
        self.code.append("nop") # Nope operation does nothing
        return None
    
    def error(self, message):
        self.code.append(f"error {message}")
        return message

    def push(self, value):
        print("push")
        self.stack.append(value)
        if type(value) == str:
            print("É Push")
            self.code.append(f"pushs \"{value}\"")
        if type(value) == int:
            self.code.append(f"pushi {value}")
        if type(value) == float:
            self.code.append(f"pushf {value}")
        return value
    
    def pop(self): 
        self.code.append("pop")
        return self.stack.pop()

    def dup(self):
        print("dup")
        value = self.stack[-1]
        self.stack.append(value)
        self.code.append("dup 1")
        return value

    def swap(self):
        #a = self.stack.pop()
        #b = self.stack.pop()
        #print("swap")
        #self.stack.append(a)
        #self.stack.append(b)
        self.code.append("swap")
        #return a, b
    
    def math(self, operator):
        b = self.stack.pop()
        a = self.stack.pop()
        print(operator)
        if operator == "+":
            result = a + b
            self.code.append("add")
        elif operator == "-":
            result = a - b
            self.code.append("sub")
        elif operator == "*":
            result = a * b
            self.code.append("mul")
        elif operator == "/":
            result = a / b
            self.code.append("div")
        elif operator == "=":
            result = a == b
            self.code.append("equal")
        elif operator == "%":
            result = a % b
            self.code.append("mod")
        elif operator == "<":
            result = a < b
            self.code.append("inf")
        elif operator == "<=":
            result = a <= b
            self.code.append("infeq")
        elif operator == ">":
            result = a > b
            self.code.append("sup")
        elif operator == ">=":
            result = a >= b
            self.code.append("supeq")
        else:
            raise ValueError("Invalid operator")
        print("math")
        self.stack.append(result)
        return result


    def print(self):
        print("print") 
        result = self.stack.pop()
        if result == int(result):
            self.code.append(f"writei") # EMIT
        elif isinstance(result, str):
            self.code.append(f"writes")
        else:
            self.code.append(f"writef")
        return result
    
    def char(self, value):
        result = ord(value)
        self.push(result)
    
    def input_key(self):
        self.code.append("read")
        self.code.append("atoi")
        return None
    
    def print_string(self, value):
        print("print_string")
        value = value[3:-1]
        self.code.append(f"pushs \"{value}\"")
        self.code.append("writes")
        return value

    def emit(self):
        self.code.append(f"writechr") 

    def cr(self):
        self.code.append("cr")

    def _if(self):
        self.code.append("if")
        return self.stack.pop()
    
    def _else(self):
        self.code.append("else")
        return self.stack.pop()
    
    def then(self):
        self.code.append("then")
        return self.stack.pop()
    
    def load(self, name, arg):
        print("load")
        self.stack.append(self.variables[name]) # Coloca as variaveis na stack
        self.code.append(f"load {arg}")
        return self.variables[name][arg]

# Conversions

    def atoi(self, value):
        print("atoi")
        self.stack.append(int(value))
        self.code.append("atoi")
        return int(value)
    
    def atof(self, value):
        print("atof")
        self.stack.append(float(value))
        self.code.append("atof")
        return float(value)
    
    def itof(self, value):
        print("itof")
        self.stack.append(float(value))
        self.code.append("itof")
        return float(value)
    
    def ftoi(self, value):
        print("ftoi")
        self.stack.append(int(value))
        self.code.append("ftoi")
        return int(value)
    
    def stri(self, value):
        print("stri")
        self.stack.append(int(value))
        self.code.append("stri")
        return int(value)
    
    def strf(self, value):
        print("strf")
        self.stack.append(float(value))
        self.code.append("strf")
        return float(value)

# Variables
    def init_var(self, name):
        print(name + "NAME")
        if name not in self.variables:
            self.variables[name] = [self.var_counter, 0]  # index and value
            self.code.insert(0, f"pushi 0")
            self.code.append(f"pushi 0")
            self.code.append(f"storeg {self.variables[name][0]}")
            self.var_counter += 1
            return name
        else:
            print(f"Variable {name} already exists")
            return None     

    def getset(self, name, value):
        if name in self.variables:
            index = self.variables[name][0]
            if value == "!":  # Set
                if self.stack:
                    self.variables[name][1] = self.stack.pop()
                    self.code.append(f"storeg {index}")
                    return name, self.variables[name][1]
                else:
                    return None
            elif value == "@":  # Get
                self.stack.append(self.variables[name][1])
                self.code.append(f"pushg {index}")
                return self.variables[name][1]
        else:
            print(f"Variable {name} does not exist")
            return None

    def space(self):
        self.code.append(f"pushs " "")
        self.code.append("writes")
        return None

    def spaces(self):
        value = self.stack.pop()
        if isinstance(value, int):
            self.code.append(f"pop")
            self.code.append(f"pushs {' ' * value}")
            self.code.append("writes")
            return ' ' * value
        else:
            return None

# Functions

    def init_func(self, count : int):
        if count != self.match_func_count:
            func = str()
            self.functions.append(func)
            self.match_func_count += 1
        else:
            return 

# Loops

    def init_loop(self, count : int):
        if count != self.match_loop_count:
            loop = str()
            self.loops.append(loop)
            self.match_loop_count += 1
        else:
            return

# Control Operations

    def pusha(self, value):
        print("pusha")
        self.stack.append(value)
        self.code.append(f"pusha {value}")
        return value
    
    def jump(self, label):
        self.code.append(f"jump {label}")
        return label
    
    def jz(self, label):
        self.code.append(f"jz {label}")
        return label
    
    def call(self, name):
        self.code.append(f"pusha {name}")
        self.code.append(f"call")
        return name

    def _return(self):
        self.code.append("return")
        return self.stack.pop()
    

    def code_to_file(self):
        filename = "../outputs/output.txt"
        with open(filename, 'w') as file:
            for line in self.code:
                file.write(f"{line}\n")
            file.write(f"stop\n")
            file.close()

    def function_to_file(self):
        filename = "../outputs/output.txt"
        with open(filename, 'a') as file:
            for line in self.code:
                file.write(f"{line}\n")
            file.write(f"return\n")
            file.close()
            
# Conditionals

    def if_then(self):
        self.code.append(f"jz ELSE{self.ifcounter}")

    def else_then(self):
        self.code.append(f"jump THEN{self.ifcounter}")
        self.code.append(f"ELSE{self.ifcounter}:")

    def only_else_then(self):
        self.code.append(f"THEN{self.ifcounter}:")
        self.ifcounter += 1