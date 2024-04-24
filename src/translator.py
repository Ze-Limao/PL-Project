class Translator:
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.code = []
        self.code.append("start")
        self.code.append("")
    
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
        self.code.append("dup")
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
        if type(result) == int:
            self.code.append("writechr")
        elif type(result) == str:
            self.code.append("writes")
        return result
    
    def char(self):
        result = self.stack.pop()
        result = ord(result[0])
        self.code.append(f"pushi {result}")
        self.code.append("writei")
    
    def print_string(self, value):
        self.code.append(f"pushs \"{value}\"")
        self.code.append("writes")
        return value
    
    def emit(self, value):
        self.code.append(f"WRITECHR {ord(value)}") 
        return value

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
    
    def function(self, name, args, body):
        self.variables[name] = (args, body)
        self.code.append(f"function {name}")
        return name
    
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
        self.code.append(f"call {name}")
        return name

    def _return(self):
        self.code.append("return")
        return self.stack.pop()
    

    def code_to_file(self):
        filename = "../outputs/output.txt"
        with open(filename, 'w') as file:
            for line in self.code:
                file.write(f"{line}\n")
            file.write(f"stop")
            file.close()
