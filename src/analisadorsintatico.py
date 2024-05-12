import ply.yacc as yacc

class Parser():
    def __init__(self, lexer, translator):
      self.lexer = lexer
      self.tokens = self.lexer.tokens
      self.parser = yacc.yacc(module=self, start='Line')
      self.translator = translator
      self.cmd_list = []
      self.func_count = 0
      self.loop_count = 0

    def parse(self, data):
        return self.parser.parse(data, lexer = self.lexer.lexer)

    ## Grammar

    def p_line(self, p):
        '''Line : Line Cmd
                | Line Function
                | 
        '''
        print("Line")
        return p
    
    def p_Expressao(self, p):
        '''Expressao : Expressao Cmd
                     |  
        '''
        print("Expressao")
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
        self.translator.getset(p[1], p[2])

    def p_get(self, p):
        '''Cmd : NAME GET '''
        p[0] = p[1]
        self.translator.getset(p[1], p[2])

    def p_swap(self, p):
        '''Cmd : SWAP'''
        print("Swap")
        p[0] = p[1]
        self.translator.swap()

    def p_init_var(self, p):
        '''Cmd : VARIABLE NAME'''
        p[0] = p[1]
        self.translator.init_var(p[2])

    def p_call(self, p):
        '''Cmd : NAME '''
        p[0] = p[1]
        self.translator.call(p[1])

    def p_input_key(self, p):
        '''Cmd : KEY'''
        p[0] = p[1]
        self.translator.input_key(p[1])

    def p_cr(self, p):
        '''Cmd : CR'''
        p[0] = p[1]
        self.translator.cr()

    def p_string(self, p):
        '''Cmd : STRING'''
        p[0] = p[1]
        self.translator.push(p[1])

    def p_print2(self, p):
        '''Cmd : EMIT
        '''
        p[0] = p[1]    
        self.translator.emit()

    def p_print(self, p):
        '''Cmd : DOT
        '''
        print("DOT")
        p[0] = p[1]
        self.translator.print()
    
    def p_char(self, p):
        '''Cmd : CHR CHAR
               | CHR MATH_OPERATOR
        '''
        p[0] = p[1]
        self.translator.char(p[2])
    
    def p_dup(self,p):
        '''Cmd : DUP        
        '''
        p[0] = p[1]
        print("YEEE")
        self.translator.dup()

    def p_printstring(self, p):
        '''Cmd : PRINTSTRING'''
        p[0] = p[1]
        self.translator.print_string(p[1])
    
    def p_char2(self, p):
        '''Cmd : CHAR'''
        print("Char")
        p[0] = p[1]
    
    def p_math_operator(self, p):
        '''Cmd : MATH_OPERATOR'''
        print("Math Operator")
        p[0] = p[1]
        self.translator.math(p[1])

    def p_loop(self, p):
        '''Cmd : Loop'''
        p[0] = p[1]

    def p_number(self, p):
        '''Cmd : NUMBER'''
        print("Number")
        p[0] = p[1]
        self.translator.push(p[1])

    def p_while(self, p):
        '''Cmd : WHILE'''
        p[0] = p[1]

    ## Condicionais 
    
    def p_if(self, p):
        '''Cmd : IF'''
        p[0] = p[1]
        self.translator.if_then() #ainda nao implementado

    def p_else(self, p):
        '''Cmd : ELSE'''
        p[0] = p[1]
        self.translator.else_then() #ainda nao implementado

    def p_only_else(self, p):
        '''Cmd : THEN'''
        p[0] = p[1]
        self.translator.only_else_then() #ainda nao implementado

    ## Loops

    def p_loop1(self, p):
        '''
        Loop : BEGIN Exloop UNTIL
        '''
        print("LOOPINHO1")
        print(p[3])
        #print(p[2] + " yee")
        
        return p

    def p_loop2(self, p):
        '''
        Loop : BEGIN Exloop REPEAT
        '''
        print("LOOPINHO2")
        #print(p[0])
        #print(p[2] + " yee")
        
        return p

    def p_loop3(self, p):
        '''
        Loop : DO Exloop LOOP
        '''
        print("LOOPINHO3")
        print(p[3])
        #print(p[2] + " yee")

        return p

    def p_loop_expression(self, p):
        """
        Exloop : Expressao
        """
        print("Exloop")
        #if len(p) == 2:
        #    print(p[1] + " MONKE")
        self.translator.init_loop(self.loop_count)
        #if name not in self.translator.functions:
        #    self.translator.functions[name] = str
        #self.translator.functions[name] += str(name)

        #print("ss" + str(len(self.name_aux)))
        for i in p:
            if i != None:
                self.translator.loops[self.loop_count] += " " + str(i)
        print(self.translator.code)

    ## Function

    def p_function(self, p):
        '''
        Function : COLON NAME Exp SEMICOLON
        '''
        print("Function")
        print(p[3])
        print(p[2] + " yee")
        
        if p[2] not in self.translator.function_names:
            self.translator.function_names.append(p[2])
            self.func_count += 1
        else:
            print(f"Function {p[2]} already exists")
            self.translator.functions[self.func_count] = ""
            return None         
        return p

    def p_function_expression(self, p):
        """
        Exp : Expressao
        """
        print("Exp")
        self.translator.init_func(self.func_count)
        #if name not in self.translator.functions:
        #    self.translator.functions[name] = str
        #self.translator.functions[name] += str(name)

        #print("ss" + str(len(self.name_aux)))
        for i in p:
            if i != None:
                self.translator.functions[self.func_count] += " " + str(i)
        print(self.translator.code)

    
    #def p_func(self, p):
    #    '''Cmd : Cmd Function
    #    '''
    #    return p

        
    def p_error(self, p):
        print("Erro de sintaxe:", p)
        self.parse.parser.exito = False
