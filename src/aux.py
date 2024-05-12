import ply.yacc as yacc

class Parser():
    def __init__(self, lexer, translator):
      self.lexer = lexer
      self.tokens = self.lexer.tokens
      self.parser = yacc.yacc(module=self, start='Cmd', debug=True)
      self.translator = translator
      self.cmd_list = []
      self.func_count = 0
      self.loop_count = 0

    def parse(self, data):
        return self.parser.parse(data, lexer = self.lexer.lexer)

    ## Grammar

    def p_line(self, p):
        '''Line : Line Expressao
                | Line Function
                | 
        '''
        return p
    
    def p_Expressao(self, p):
        '''Expressao : Cmd
                     | Expressao Cmd 
        '''
        return p

    def p_comment1(self, p):
        '''Cmd : Cmd COMMENT1'''
        pass

    def p_comment2(self, p):
        '''Cmd : Cmd COMMENT2'''
        pass

    def p_set(self, p):
        '''Cmd : Cmd NAME SET '''
        p[0] = p[1]
        self.translator.getset(p[2], p[3])

    def p_get(self, p):
        '''Cmd : Cmd NAME GET '''
        p[0] = p[1]
        self.translator.getset(p[2], p[3])

    def p_swap(self, p):
        '''Cmd : Cmd SWAP'''
        print("Swap")
        p[0] = p[1]
        self.translator.swap()

    def p_do(self, p):
        '''Cmd : Cmd NUMBER DO'''
        p[0] = p[1]
        self.translator.do(p[2])

    #def p_lp(self, p):
    #    '''Cmd : Cmd LOOP
    #    '''
    #    p[0] = p[1]
    #    return p

    def p_init_var(self, p):
        '''Cmd : Cmd VARIABLE NAME'''
        p[0] = p[1]
        self.translator.init_var(p[3])

    def p_call(self, p):
        '''Cmd : Cmd NAME '''
        p[0] = p[1]
        self.translator.call(p[2])

    def p_input_key(self, p):
        '''Cmd : Cmd KEY'''
        p[0] = p[1]
        self.translator.input_key(p[2])

    def p_cr(self, p):
        '''Cmd : Cmd CR'''
        p[0] = p[1]
        self.translator.cr()

    def p_string(self, p):
        '''Cmd : Cmd STRING'''
        p[0] = p[1]
        self.translator.push(p[2])

    def p_print2(self, p):
        '''Cmd : Cmd EMIT
        '''
        p[0] = p[1]    
        self.translator.emit()

    def p_print(self, p):
        '''Cmd : Cmd DOT
        '''
        p[0] = p[1]
        self.translator.print()
    
    def p_char(self, p):
        '''Cmd : Cmd CHR CHAR
               | Cmd CHR MATH_OPERATOR
        '''
        p[0] = p[1]
        self.translator.char(p[3])
    
    def p_dup(self,p):
        '''Cmd : Cmd DUP        
        '''
        p[0] = p[1]
        self.translator.dup()

    def p_printstring(self, p):
        '''Cmd : Cmd PRINTSTRING'''
        p[0] = p[1]
        self.translator.print_string(p[2])

    def p_number(self, p):
        '''Cmd : Cmd NUMBER'''
        print("Number")
        p[0] = p[2]
        self.translator.push(p[2])
    
    def p_char2(self, p):
        '''Cmd : Cmd CHAR'''
        print("Char")
        p[0] = p[2]
    
    def p_math_operator(self, p):
        '''Cmd : Cmd MATH_OPERATOR'''
        print("Math Operator")
        p[0] = p[2]
        self.translator.math(p[2])

    def p_loop(self, p):
        '''Cmd : Cmd Loop'''
        p[0] = p[1]

    def p_while(self, p):
        '''Cmd : Cmd WHILE'''
        p[0] = p[1]

    def p_cmdEmpty(self, p):
        '''Cmd : '''
        pass

    ## Loops

    def p_loop1(self, p):
        '''
        Loop : NUMBER BEGIN Exloop UNTIL
        '''
        print("LOOPINHO")
        print(p[3])
        print(p[2] + " yee")
        self.translator.push(p[1])
        return p

    def p_loop2(self, p):
        '''
        Loop : NUMBER BEGIN Exloop REPEAT
        '''
        print("LOOPINHO")
        print(p[2] + " yee")
        self.translator.push(p[1])
        
        return p

    def p_loop3(self, p):
        '''
        Loop : NUMBER DO Exloop LOOP
        '''
        print("LOOPINHO")
        print(p[3])
        print(p[2] + " yee")
        self.translator.push(p[1])

        return p

    def p_loop_expression(self, p):
        """
        Exloop : Exloop NUMBER
               | Exloop CHR CHAR
               | Exloop CHR MATH_OPERATOR
               | Exloop DUP
               | Exloop CHAR
               | Exloop MATH_OPERATOR
               | Exloop EMIT
               | Exloop STRING
               | Exloop DOT
               | Exloop PRINTSTRING
               | Exloop CR
               | Exloop KEY
               | Exloop NAME
               | Exloop VARIABLE NAME
               | Exloop NAME GET
               | Exloop NAME SET
               | Exloop SWAP
               | Exloop WHILE
               | Loop 
               | 
            
        """
        print("Exloop")
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
        Exp : Exp NUMBER
            | Exp CHR CHAR
            | Exp CHR MATH_OPERATOR
            | Exp DUP
            | Exp CHAR
            | Exp MATH_OPERATOR
            | Exp EMIT
            | Exp STRING
            | Exp DOT
            | Exp PRINTSTRING
            | Exp CR
            | Exp KEY
            | Exp NAME
            | Exp VARIABLE NAME
            | Exp NAME GET
            | Exp NAME SET
            | Exp SWAP
            | Exp WHILE
            | Exp Loop
            | 
            
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

    
    def p_func(self, p):
        '''Cmd : Cmd Function
        '''
        return p

        
    def p_error(self, p):
        print("Erro de sintaxe:", p)
        self.parse.parser.exito = False
