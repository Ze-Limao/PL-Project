class Translator:
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.functions = {}
        self.code = []
        self.code.append("start")
        self.code.append("")
        self.var_counter = 0
    
    def nop(self):
        self.code.append("nop") # Nope operation does nothing
        return None
    
    def error(self, message):
        self.code.append(f"error {message}")
        return message

    def push(self, value):
        self.stack.append(value)
        if type(value) == str:
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
        value = self.stack[-1]
        self.stack.append(value)
        self.code.append("dup 1")
        return value

    def swap(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a)
        self.stack.append(b)
        self.code.append("swap")
        return a, b
    
    def math(self, operator):
        b = self.stack.pop()
        a = self.stack.pop()
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
        elif operator == "==":
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
        self.stack.append(result)
        return result


    def print(self): 
        result = self.stack.pop()
        if isinstance(result, int):
            self.code.append(f"writei") # EMIT
        elif isinstance(result, str):
            self.code.append(f"writes")
        return result
    
    def char(self, value):
        result = ord(value)
        self.push(result)
    
    def input_key(self):
        self.code.append("read")
        self.code.append("atoi")
        return None
    
    def print_string(self, value):
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
        self.stack.append(self.variables[name]) # Coloca as variaveis na stack
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
    def init_var(self, name):
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

# Functions

    def init_func(self, name, body):
        if name not in self.functions:
            self.functions[name] = (f"{body}")
            return name
        else:
            print(f"Function {name} already exists")
            return None 


# Control Operations

    def pusha(self, value):
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