class Translator:
    def __init__(self):
        self.stack = []
        self.variables = {}
        self.code = []
        self.code.append("start")
        self.code.append("")
    
    def forth_push(self, value):
        self.stack.append(value)
        self.code.append(f"push {value}")
        return value
    
    def forth_math(self, operator):
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
            self.code.append("equals")
        elif operator == "%":
            result = a % b
            self.code.append("mod")
        elif operator == "<":
            result = a < b
            self.code.append("less")
        elif operator == ">":
            result = a > b
            self.code.append("greater")
        else:
            raise ValueError("Invalid operator")
        self.stack.append(result)
        return result

    def forth_pop(self):
        return self.stack.pop()
    
    def forth_print(self):
        self.code.append("print")
        result = self.stack.pop()
        return result
    
    def forth_if(self):
        self.code.append("if")
        return self.stack.pop()
    
    def forth_else(self):
        self.code.append("else")
        return self.stack.pop()
    
    def forth_then(self):
        self.code.append("then")
        return self.stack.pop()
    
    def forth_function(self, name, args, body):
        self.variables[name] = (args, body)
        self.code.append(f"function {name}")
        return name
    
    def forth_swap(self):
        a = self.stack.pop()
        b = self.stack.pop()
        self.stack.append(a)
        self.stack.append(b)
        self.code.append("swap")
        return a, b


    def code_to_file(self):
        filename = "output.txt"
        with open(filename, 'w') as file:
            for line in self.code:
                file.write(f"{line}\n")
