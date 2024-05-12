import ply.yacc as yacc

class Parser():
    def __init__(self, lexer, translator):
      self.lexer = lexer
      self.tokens = self.lexer.tokens
      self.parser = yacc.yacc(module=self, start='Line')
      self.translator = translator
      self.func_count = 0
      self.in_func = False
      self.in_loop = False

    def parse(self, data):
        return self.parser.parse(data, lexer = self.lexer.lexer)

    ## Grammar

    def p_line(self, p):
        '''Line : Line Cmd
                | Line Function
                | 
        '''
        return p
    
    def p_Expressao(self, p):
        '''Expressao : Expressao Cmd
                     |  
        '''
        return p

    def p_comment1(self, p):
        '''Cmd : COMMENT1'''
        pass

    def p_comment2(self, p):
        '''Cmd : COMMENT2'''
        pass

    def p_set(self, p):
        '''Cmd : NAME SET '''
        p[0] = p[1]
        self.translator.getset(p[1], p[2], self.in_func, self.in_loop)

    def p_get(self, p):
        '''Cmd : NAME GET '''
        p[0] = p[1]
        self.translator.getset(p[1], p[2], self.in_func, self.in_loop)

    def p_swap(self, p):
        '''Cmd : SWAP'''
        p[0] = p[1]
        self.translator.swap(self.in_func, self.in_loop)

    def p_init_var(self, p):
        '''Cmd : VARIABLE NAME'''
        p[0] = p[1]
        self.translator.init_var(p[2], self.in_func, self.in_loop)

    def p_call(self, p):
        '''Cmd : NAME '''
        p[0] = p[1]
        self.translator.call(p[1], self.in_func, self.in_loop)

    def p_input_key(self, p):
        '''Cmd : KEY'''
        p[0] = p[1]
        self.translator.input_key(self.in_func, self.in_loop)

    def p_cr(self, p):
        '''Cmd : CR'''
        p[0] = p[1]
        self.translator.cr(self.in_func, self.in_loop)

    def p_string(self, p):
        '''Cmd : STRING'''
        p[0] = p[1]
        self.translator.push(p[1], self.in_func, self.in_loop)

    def p_print2(self, p):
        '''Cmd : EMIT
        '''
        p[0] = p[1]    
        self.translator.emit(self.in_func, self.in_loop)

    def p_print(self, p):
        '''Cmd : DOT
        '''
        p[0] = p[1]
        self.translator.print(self.in_func, self.in_loop)
    
    def p_char(self, p): #Possivelmente vai sair
        '''Cmd : CHR CHAR
               | CHR MATH_OPERATOR
        '''
        p[0] = p[1]
        self.translator.char(p[2])
    
    def p_dup(self,p):
        '''Cmd : DUP        
        '''
        p[0] = p[1]
        self.translator.dup(self.in_func, self.in_loop)

    def p_printstring(self, p):
        '''Cmd : PRINTSTRING'''
        p[0] = p[1]
        self.translator.print_string(p[1],self.in_func, self.in_loop)
    
    def p_char2(self, p):
        '''Cmd : CHAR'''
        p[0] = p[1]
    
    def p_math_operator(self, p):
        '''Cmd : MATH_OPERATOR'''
        p[0] = p[1]
        self.translator.math(p[1], self.in_func, self.in_loop)

    def p_loop(self, p):
        '''Cmd : Loop'''
        p[0] = p[1]

    def p_number(self, p):
        '''Cmd : NUMBER'''
        p[0] = p[1]
        self.translator.push(p[1], self.in_func, self.in_loop)

    ## Condicionais 
    
    def p_if(self, p):
        '''Cmd : IF'''
        p[0] = p[1]
        self.translator.if_then(self.in_func,self.in_loop) #ainda nao implementado

    def p_else(self, p):
        '''Cmd : ELSE'''
        p[0] = p[1]
        self.translator.else_then(self.in_func,self.in_loop) #ainda nao implementado

    def p_only_else(self, p):
        '''Cmd : THEN'''
        p[0] = p[1]
        self.translator.only_else_then(self.in_func,self.in_loop) #ainda nao implementado

    ## Loops

    def p_begin(self, p):
        '''Begin : BEGIN'''
        p[0] = p[1]
        self.in_loop = True
        self.translator.init_loop()

    def p_until(self, p):
        '''Until : UNTIL'''
        p[0] = p[1]
        self.translator.until()

    def p_do(self, p):
        '''Do : DO'''
        p[0] = p[1]
        self.in_loop = True
        self.translator.init_loop()

    def p_while(self, p):
        '''Cmd : WHILE'''
        p[0] = p[1]
        self.translator._while()

    def p_Repeat(self, p):
        '''Repeat : REPEAT'''
        p[0] = p[1]
        self.translator.repeat()
    
    def p_endLoop(self, p):
        '''LooP : LOOP
        '''
        self.translator.until()
        return p
    
    def p_loop1(self, p):
        '''
        Loop : Begin Expressao Until
        '''
        self.in_loop = False
        
        return p

    def p_loop2(self, p):
        '''
        Loop : Begin Expressao Repeat
        '''
        self.in_loop = False
        
        return p

    def p_loop3(self, p):
        '''
        Loop : Do Expressao LooP
        '''
        self.in_loop = False

        return p

    def p_colon(self, p):
        '''Colon : COLON'''
        p[0] = p[1]
        self.in_func = True
        self.translator.init_func()

    def p_function(self, p):
        '''
        Function : Colon NAME Expressao SEMICOLON
        '''
        self.in_func = False
        
        if p[2] not in self.translator.function_names:
            self.translator.function_names.append(p[2])
        else:
            print(f"Function {p[2]} already exists")
            self.translator.functions[self.func_count] = ""
            return None         
        return p

        
    def p_error(self, p):
        print("Erro de sintaxe:", p)
        self.parse.parser.exito = False
