import lexical_analyzer


print_switch = True
token_index = 0
peek_next_index = 0

token = []
lexeme = []

with open('output_file.txt', 'r') as file:
    while True:
        contents = file.readline()
        if not contents:
            break
        temp = contents.split()
        token.append(temp[0])
        lexeme.append(temp[1])

#i = 0
#for i in range(len(token)):
    #print(token[i], lexeme[i])


#Error handler
def error_handler(token, lexeme, rule):
    rule += 1
    print('\nThere is an error on line {0}'.format(rule))
    print('Token: {0}   Lexeme: {1}'.format(token, lexeme))

def update_output(token, lexeme, rule):
    with open('syntax_output_file.txt', 'a') as file:
        file.write('\nToken: {0}      Lexeme: {1} \n'.format(token, lexeme))
        file.write(rule + '\n')



#R1. <Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $
def Rat24S():
    global token_index
    if print_switch:
        print("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
    
    update_output(token[token_index], lexeme[token_index], "<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
    if lexeme[token_index] == '$':
        token_index += 1
        update_output(token[token_index], lexeme[token_index], "<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
        print('40:', lexeme[token_index])
        if lexeme[token_index] == 'function':
            Optional_Function_Definitions()
            print('44:', lexeme[token_index])
            token_index += 1
            print('49:', lexeme[token_index])
            update_output(token[token_index], lexeme[token_index], "<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
            if lexeme[token_index] == '$':
                if (token_index + 1) == len(token):
                    return
            elif lexeme[token_index] == 'function':
                Optional_Function_Definitions()
                
            else:
                error_handler(token[token_index],lexeme[token_index], token_index)
                exit(1)
        elif lexeme[token_index] == 'integer' or lexeme[token_index] == 'boolean' or lexeme[token_index] == 'real':
            Optional_Declaration_List()
            update_output(token[token_index], lexeme[token_index], "<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
            token_index += 1
            update_output(token[token_index], lexeme[token_index], "<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
            if lexeme[token_index] == '$':
                if (token_index + 1) == len(token):
                    return
            else:
                error_handler(token[token_index],lexeme[token_index], token_index)
                exit(1)
        #Is never getting called because the optional function definition is not finishing w '$' -> error handler
        #token_index += 1
        update_output(token[token_index], lexeme[token_index], "<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
        Statement_List()
        update_output(token[token_index], lexeme[token_index], "<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
        token_index += 1
        update_output(token[token_index], lexeme[token_index], "<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
        if not lexeme[token_index] == '$':
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)     
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

#R2. <Opt Function Definitions> ::= <Function Definitions> | <Empty>
def Optional_Function_Definitions():
    global token_index
    if print_switch:
        print("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")

    print('76:', lexeme[token_index])
    update_output(token[token_index], lexeme[token_index], "<Opt Function Definitions> ::= <Function Definitions> | <Empty>")
    
    if lexeme[token_index] == 'function':
        Function_Definition()
    elif token[token_index] == 'Unknown':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)
    else:
        Empty()
#R3. Original: <Function Definitions> ::= <Function> | <Function> <Function Definitions>
#-> Factorized: <Function Definition> ::= <Function> <Function Definition Prime>
def Function_Definition():
    global token_index
    if print_switch:
        print("Original: <Function Definitions> ::= <Function> | <Function> <Function Definitions>")
        print("-> Factorized: <Function Definition> ::= <Function> <Function Definition Prime>")

    update_output(token[token_index], lexeme[token_index], "<Function Definition> ::= <Function> <Function Definition Prime>")
    print('97:', lexeme[token_index])
    Function()
    print('100:', lexeme[token_index])
    Function_Definition_Prime()

#<Function Definition Prime> ::= <Function Definition> | <Empty>
def Function_Definition_Prime():
    global token_index
    if print_switch:
        print("<Function Definition Prime> ::= <Function Definition> | <Empty>")
    
    update_output(token[token_index], lexeme[token_index], "<Function Definition Prime> ::= <Function Definition> | <Empty>")
    print('109:', lexeme[token_index])
    if lexeme[token_index] == 'function':
        print('Func_Def_Prime', token[token_index], lexeme[token_index])
        Function_Definition()
        print('115:', lexeme[token_index])
    elif lexeme[token_index] == '}':
        print('117:', lexeme[token_index])
        return
    elif lexeme[token_index] == '{':
        Function_Definition()
    elif token[token_index] == 'Identifier' or token[token_index] == 'Operator' or token[token_index] == 'Keywords' or token[token_index] == 'Separators':
        print('118:', lexeme[token_index])
        Function_Definition()
    elif token[token_index] == 'Unknown':
        print('122:', lexeme[token_index])
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)
    else:
        print('119:', lexeme[token_index])
        Empty()

#R4. <Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>
def Function():
    global token_index
    if print_switch:
        print("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
    
    update_output(token[token_index], lexeme[token_index], "<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
    
    print('128:', lexeme[token_index])
    if lexeme[token_index] == "function":
        token_index += 1
        print('131:', lexeme[token_index])
        if token[token_index] == 'Identifier':
            token_index += 1
            print('134:', lexeme[token_index])
            if lexeme[token_index] == '(':
                print('150:', lexeme[token_index])
                token_index += 1
                print('152:', lexeme[token_index])
                Optional_Parameter_List()
                token_index += 1
                print('155:', lexeme[token_index])
                if lexeme[token_index] == ')':
                    token_index += 1
                else:
                    error_handler(token[token_index],lexeme[token_index], token_index)
                    exit(1)
               
                print('158:', lexeme[token_index])
                Optional_Declaration_List()
                print('162:', lexeme[token_index])
                Body()
                print('164:', lexeme[token_index])
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1) 

#R5. <Opt Parameter List> ::= <Parameter List> | <Empty>
def Optional_Parameter_List():
    global token_index
    if print_switch:
        print("<Opt Parameter List> ::= <Parameter List> | <Empty>")

    update_output(token[token_index], lexeme[token_index], "<Opt Parameter List> ::= <Parameter List> | <Empty>")
    print('169:', lexeme[token_index])
    if token[token_index] == 'Identifier':
        Parameter_List()
    elif token[token_index] == 'Unknown':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)
    else:
        print('179:', lexeme[token_index])
        Empty()


#R6. Original: <Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>
#-> Factorized: <Parameter List> ::= <Parameter> <Parameter List Prime>
def Parameter_List():
    global token_index
    if print_switch:
        print("Original: <Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>")
        print("-> Factorized: <Parameter List> ::= <Parameter> <Parameter List Prime>")
    update_output(token[token_index], lexeme[token_index], "<Parameter List> ::= <Parameter> <Parameter List Prime>")
    print('175:', lexeme[token_index])
    Parameter()
    print('177:', lexeme[token_index])
    Parameter_List_Prime()



#<Parameter List Prime> ::= <Parameter List> | <Empty> 
def Parameter_List_Prime():
  global token_index
  if print_switch:
    print("<Parameter List Prime> ::= <Parameter List> | <Empty>")

    peek_next_index = token_index
    peek_next_index += 1
    update_output(token[token_index], lexeme[token_index], "<Parameter List Prime> ::= <Parameter List> | <Empty>")
    print('187:', lexeme[token_index])
    if token[token_index] == 'Identifier':
        Parameter_List()
    elif lexeme[peek_next_index] == ',':
        token_index += 2
        Parameter_List() 
    elif token[token_index] == 'Unknown':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)
    else:
        Empty()

#R7. <Parameter> ::= <IDs> <Qualifier>
def Parameter():
    global token_index
    if print_switch:
        print("<Parameter> ::= <IDs> <Qualifier>")
    update_output(token[token_index], lexeme[token_index], "<Parameter> ::= <IDs> <Qualifier>")
    print('200:', lexeme[token_index])
    IDs()
    print('202:', lexeme[token_index])
    token_index += 1
    Qualifier()


# R8. <Qualifier> ::= integer | boolean | real
def Qualifier():
    global token_index
    if print_switch:
        print("<Qualifier> ::= integer | boolean | real")
    
    update_output(token[token_index], lexeme[token_index], "<Qualifier> ::= integer | boolean | real")

    print('229:', lexeme[token_index])
    #token_index += 1
    print('231:', lexeme[token_index])
    lexer = lexeme[token_index]

    if not (lexer == 'integer' or lexer == 'boolean' or lexer == 'real'):
        print("Error: Expected 'integer', 'boolean', or 'real' in Qualifier")
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)    
    else:
        print('235:', lexeme[token_index])
        return
        #token_index += 1
        print('237:', lexeme[token_index])
        

# R9. <Body> ::= { <Statement List> }
def Body():
    global token_index
    if print_switch:
        print("<Body> ::= { <Statement List> }")
    update_output(token[token_index], lexeme[token_index], "<Body> ::= { <Statement List> }")
    print('251', lexeme[token_index])
    if lexeme[token_index] == '{':
        token_index += 1
        print('254', lexeme[token_index])
        Statement_List()
        token_index += 1
        print('279', lexeme[token_index])
        if not lexeme[token_index] == '}':
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)   
        else:
            return      


#R10. <Opt Declaration List> ::= <Declaration List> | <Empty>
def Optional_Declaration_List():
    global token_index
    if print_switch:
        print("<Opt Declaration List> ::= <Declaration List> | <Empty>")

    update_output(token[token_index], lexeme[token_index], "<Opt Declaration List> ::= <Declaration List> | <Empty>")
    lexer = lexeme[token_index]
    print("268:", lexer)
    if lexer == 'integer' or lexer == 'boolean' or lexer == 'real':
        Declaration_List()
    elif token[token_index] == 'Unknown':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)       
    else:
        Empty()

# R11. <Declaration List> ::= <Declaration> ; <Declaration List Prime>
def Declaration_List():
    global token_index
    if print_switch:
        print("<Declaration List> ::= <Declaration> ; <Declaration List Prime>")
    update_output(token[token_index], lexeme[token_index], "<Declaration> ; <Declaration List Prime>")

    Declaration()
    token_index += 1
    if lexeme[token_index] == ';':
            token_index += 1
            Declaration_List_Prime()
    else:
        print("Missing semicolon (;) after declaration")
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)  

# <Declaration List Prime> ::= <Declaration List> | <Empty>
def Declaration_List_Prime():
    global token_index
    if print_switch:
        print("<Declaration List Prime> ::= <Declaration List> | <Empty>")

    update_output(token[token_index], lexeme[token_index], "<Declaration List Prime> ::= <Declaration List> | <Empty>")

    lexer = lexeme[token_index]
    if lexer == 'integer' or lexer == 'boolean' or lexer == 'real':
        Declaration_List()
    elif token[token_index] == 'Unknown':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)       
    else:
        Empty() 


# R12. <Declaration> ::= <Qualifier> <IDs>
def Declaration():
    global token_index
    if print_switch:
        print("<Declaration> ::= <Qualifier> <IDs>")
    update_output(token[token_index], lexeme[token_index], "<Declaration> ::= <Qualifier> <IDs>")
    print('353', lexeme[token_index])
    Qualifier()
    print('355', lexeme[token_index])
    token_index += 1
    IDs()
    print('357', lexeme[token_index])

#R13. Original: <IDs> ::= <Identifier> | <Identifier>, <IDs>
#-> Factorized: <IDS> ::= <Identifier> <IDs Prime>
def IDs():
    global token_index
    if print_switch:
        print("Original: <IDs> ::= <Identifier> | <Identifier>, <IDs>")
        print("-> Factorized: <IDS> ::= <Identifier> <IDs Prime>")
    update_output(token[token_index], lexeme[token_index], "<IDS> ::= <Identifier> <IDs Prime>")

    peek_next_index = token_index
    peek_next_index += 1

    print('301:', token[token_index], lexeme[token_index])
    if token[token_index] == 'Identifier':
        if lexeme[peek_next_index] == ',':
            print('366', lexeme[peek_next_index])
            token_index += 1
        IDs_Prime()

    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)


#<IDs Prime> ::= , <IDs> | <Empty> 
def IDs_Prime():
    global token_index
    if print_switch:
        print("<IDs Prime> ::= , <IDs> | <Empty>")
    update_output(token[token_index], lexeme[token_index], "<IDs Prime> ::= <IDs> | <Empty>")

    if lexeme[token_index] == ',':
        token_index += 1
        IDs()      
    elif token[token_index] == 'Unknown':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)
    else:
        Empty()

#R14. Original: <Statement List> ::= <Statement> | <Statement> <Statement List>
#-> Factorized: <Statement List> ::= <Statement> <Statement List Prime>
def Statement_List():
    global token_index
    if print_switch:
        print("Original: <Statement List> ::= <Statement> | <Statement> <Statement List>")
        print("-> Factorized: <Statement List> ::= <Statement> <Statement List Prime>")
    update_output(token[token_index], lexeme[token_index], "<Statement List> ::= <Statement> <Statement List Prime>")
    Statement()
    Statement_List_Prime()

#<Statement List Prime> ::= <Statement List> | <Empty>
def Statement_List_Prime():
    global token_index
    global peek_next_index
    if print_switch:
        print("<Statement List Prime> ::= <Statement List> | <Empty>")

    update_output(token[token_index], lexeme[token_index], "<Statement List Prime> ::= <Statement List> | <Empty>")

    peek_next_index = token_index
    peek_next_index += 1

    if lexeme[token_index] == ';' and lexeme[peek_next_index] != '}':
        token_index += 1
        print('425', lexeme[token_index], token[token_index])

    print('427', lexeme[token_index], token[token_index])

    lexer = lexeme[token_index]
    t = token[token_index]

    if lexer == '{' or t == 'Identifier' or lexer == 'if' or lexer == 'return' or lexer == 'print' or lexer == 'scan' or lexer == 'while':
        print('433', lexeme[token_index], token[token_index])
        Statement_List()
    elif token[token_index] == 'Unknown':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)
    else:
        Empty()

#R15. <Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>
def Statement():
    global token_index
    print("<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>")
    print('380', lexeme[token_index], token[token_index])

    update_output(token[token_index], lexeme[token_index], "<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>")
    if lexeme[token_index] == '{':
        Compound()
    elif token[token_index] == 'Identifier':
        Assign()
    elif lexeme[token_index] == 'if':
        If()
    elif lexeme[token_index] == 'return' :
        Return()
    elif lexeme[token_index] == 'print':
        Print()
    elif lexeme[token_index] == 'scan' :
        Scan()
    elif lexeme[token_index] == 'while':
        While()
    else:
        print("Syntax Error: Invalid statement")
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

#R16. <Compound> ::= { <Statement List> }
def Compound():
    global token_index
    if print_switch:
        print("<Compound> ::= { <Statement List> }")

    update_output(token[token_index], lexeme[token_index], "<Compound> ::= { <Statement List> }")

    if lexeme[token_index] == '{':
        token_index += 1
        update_output(token[token_index], lexeme[token_index], "<Compound> ::= { <Statement List> }")
        Statement_List()
        token_index += 1
        update_output(token[token_index], lexeme[token_index], "<Compound> ::= { <Statement List> }")
        if not lexeme[token_index] == '}':
            print("error in Compound")
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)


#R17. <Assign> ::= <Identifier> = <Expression> ;
def Assign():
    global token_index
    if print_switch:
        print("<Assign> ::= <Identifier> = <Expression> ;")
    
    update_output(token[token_index], lexeme[token_index], "<Assign> ::= <Identifier> = <Expression> ;")

    print('423', lexeme[token_index], token[token_index])
    if token[token_index] == 'Identifier':
        token_index += 1
        print('426', lexeme[token_index], token[token_index])
        if lexeme[token_index] == '=':
            token_index += 1
            print('429', lexeme[token_index], token[token_index])
            Expression()
            token_index += 1
            print('447', lexeme[token_index], token[token_index])
            if lexeme[token_index] == ';':
                return
            else:
                error_handler(token[token_index],lexeme[token_index], token_index)
                exit(1)


# R18. <If> ::= if ( <Condition> ) <Statement> <If Prime>
def If():
    global token_index
    if print_switch:
        print("<If> ::= if ( <Condition> ) <Statement> <If Prime>")
    
    print('518', lexeme[token_index])
    update_output(token[token_index], lexeme[token_index], "<If> ::= if ( <Condition> ) <Statement> <If Prime>")
    if lexeme[token_index] == 'if':
        token_index += 1
        print('522', lexeme[token_index])
        if lexeme[token_index] == '(':
            token_index += 1
            print('525', lexeme[token_index])
            Condition()
            print('527', lexeme[token_index])
            token_index += 1
            print('529', lexeme[token_index])
            if lexeme[token_index] == ')':
                token_index += 1
                print('532', lexeme[token_index])
                Statement()
                print('534', lexeme[token_index])
                token_index += 1
                print('536', lexeme[token_index])
                If_Prime()
                token_index += 1
                print('538', lexeme[token_index])
            else:
                error_handler(token[token_index],lexeme[token_index], token_index)
                exit(1)   
        else:
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

# <If Prime> ::= else <Statement> endif | endif
def If_Prime():
    global token_index
    if print_switch:
        print("<If Prime> ::= else <Statement> endif | endif")
    update_output(token[token_index], lexeme[token_index], "<If Prime> ::= else <Statement> endif | endif")

    print('550', lexeme[token_index])
    if lexeme[token_index] == 'else':
        token_index += 1
        print('553', lexeme[token_index])
        Statement()
        print('555', lexeme[token_index])
        token_index += 1
        print('557', lexeme[token_index])
        if not lexeme[token_index] == 'endif':
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)
    elif not lexeme[token_index] == 'endif':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

#R19. <Return> ::= return <Return Prime>
def Return():
    global token_index
    if print_switch:
        print("<Return> ::= return <Return Prime>")
    
    update_output(token[token_index], lexeme[token_index], "<Return> ::= return <Return Prime>")

    print('505', lexeme[token_index], token[token_index])
    if lexeme[token_index] == 'return':
        token_index += 1
        print('507', lexeme[token_index], token[token_index])
        Return_Prime()
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

# <Return Prime> ::= <Expression>; | <Empty>;
def Return_Prime():
    global token_index
    if print_switch:
        print("<Return Prime> ::= <Expression>; | <Empty>;")
    
    update_output(token[token_index], lexeme[token_index], "<Return Prime> ::= <Expression>; | <Empty>;")

    print('522', lexeme[token_index], token[token_index])

    lexer = lexeme[token_index]
    t = token[token_index]

    if lexer == ';':
        #token_index += 1
        print('529', lexeme[token_index], token[token_index])
        Empty()
    elif t == 'Identifier' or t == 'Integer' or lexer == '(' or t == 'Real' or lexer == 'true' or lexer == 'false':
        print('538', lexeme[token_index], token[token_index])
        Expression()
        token_index += 1
        print('540', lexeme[token_index], token[token_index])
        if lexeme[token_index] == ';':
            return
        else:
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)
    elif token[token_index] == 'Unknown':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

# R20. <Print> ::= print ( <Expression> );
def Print():
    global token_index
    if print_switch:
        print("<Print> ::= print ( <Expression> );")
    update_output(token[token_index], lexeme[token_index], "<Print> ::= print ( <Expression> );")

    if lexeme[token_index] == 'print':
        token_index += 1
        if lexeme[token_index] == '(':
            token_index += 1
            Expression()
            token_index += 1
            if lexeme[token_index] == ')':
                    token_index += 1
                    if not lexeme[token_index] == ';':
                        print("Error: Missing semicolon (;) after print statement")
                        error_handler(token[token_index],lexeme[token_index], token_index)
                        exit(1)
            else:
                error_handler(token[token_index],lexeme[token_index], token_index)
                exit(1)
        else:
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)       
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

# R21. <Scan> ::= scan ( <IDs> );
def Scan():
    global token_index
    if print_switch:
        print("<Scan> ::= scan ( <IDs> );")
    
    update_output(token[token_index], lexeme[token_index], "<Scan> ::= scan ( <IDs> );")

    if lexeme[token_index] == 'scan':
        token_index += 1
        if lexeme[token_index] == '(':
            token_index += 1
            IDs()
            token_index += 1
            if lexeme[token_index] == ')':
                token_index += 1
                if not lexeme[token_index] == ';':
                    error_handler(token[token_index],lexeme[token_index], token_index)
                    exit(1)
                else:
                    error_handler(token[token_index],lexeme[token_index], token_index)
                    exit(1)
            else:
                error_handler(token[token_index],lexeme[token_index], token_index)
                exit(1)
        else:
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

# R22. <While> ::= while ( <Condition> ) <Statement> endwhile
def While():
    global token_index
    if print_switch:
        print("<While> ::= while ( <Condition> ) <Statement> endwhile")

    update_output(token[token_index], lexeme[token_index], "<While> ::= while ( <Condition> ) <Statement> endwhile")

    if lexeme[token_index] == 'while':
        token_index += 1
        if lexeme[token_index] == '(':
            token_index += 1
            Condition()
            token_index += 1
            if lexeme[token_index] == ')':
                token += 1
                Statement()
                if not lexeme[token_index] == 'endwhile':
                    error_handler(token[token_index],lexeme[token_index], token_index)
                    exit(1)
            else:
                error_handler(token[token_index],lexeme[token_index], token_index)
                exit(1)
        else:
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

            

#R23. <Condition> ::= <Expression> <Relop> <Expression>
def Condition():
    global token_index
    if print_switch:
        print("<Condition> ::= <Expression> <Relop> <Expression>")
    
    update_output(token[token_index], lexeme[token_index], "<Condition> ::= <Expression> <Relop> <Expression>")
    
    print('708', lexeme[token_index])
    Expression()
    print('710', lexeme[token_index])
    token_index += 1
    print('712', lexeme[token_index])
    Relop()
    print('714', lexeme[token_index])
    token_index += 1
    print('716', lexeme[token_index])
    Expression()
    print('718', lexeme[token_index])


#R24. <Relop> ::= == | != | > | < | <= | =>
def Relop():
    global token_index
    if print_switch:
        print("<Relop> ::= == | != | > | < | <= | =>")
    update_output(token[token_index], lexeme[token_index], "<Relop> ::= == | != | > | < | <= | =>")
    #token_index += 1
    print('728', lexeme[token_index])
    if lexeme[token_index] == '==' or lexeme[token_index] == '!=' or lexeme[token_index] == '>' or lexeme[token_index] == '<' or lexeme[token_index] == '<=' or lexeme[token_index] == '>=':
        return
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)

# R25. <Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>
# Revised: <Expression> ::= <Term> <Expression_Prime>
def Expression():
    global token_index
    if print_switch:
        print("<Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>")
        print("Revised: <Expression> ::= <Term> <Expression_Prime>")  
    update_output(token[token_index], lexeme[token_index], "<Expression> ::= <Term> <Expression_Prime>")

    print('621', lexeme[token_index], token[token_index])
    Term()
    print('623', lexeme[token_index], token[token_index])
    Expression_Prime()


#<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>
def Expression_Prime():
    global peek_next_index
    global token_index
    if print_switch:
        print("<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>")
    
    update_output(token[token_index], lexeme[token_index], "<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>")

    peek_next_index = token_index
    peek_next_index += 1

    print('664', lexeme[token_index], token[token_index])
    print('667 peek next', lexeme[peek_next_index], token[peek_next_index])
    if lexeme[peek_next_index] == '+' or lexeme[peek_next_index] == '-':
        token_index += 1

    #token_index += 1
    update_output(token[token_index], lexeme[token_index], "<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>")

    lexer = lexeme[token_index]
    print('638', lexeme[token_index], token[token_index])
    if lexer == '+' or lexer == '-':
        token_index += 1
        print('643', lexeme[token_index], token[token_index])
        Term()
        print('645', lexeme[token_index], token[token_index])
        Expression_Prime()
    elif token[token_index] == 'Unknown':
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)
    else:
        Empty()
        

#R26. Original: <Term> ::= <Term> * <Factor> | <Term> / <Factor> | <Factor>
#Revised: <Term> ::= <Factor> <Term Prime>
def Term():
    global token_index
    if print_switch:
        print("Original: <Term> ::= <Term> * <Factor> | <Term> / <Factor> | <Factor>")
        print("Revised: <Term> ::= <Factor> <Term Prime>")
    update_output(token[token_index], lexeme[token_index], "<Term> ::= <Factor> <Term Prime>")

    print('651', lexeme[token_index], token[token_index])
    Factor()
    print('653', lexeme[token_index], token[token_index])
    Term_Prime()

#<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>
def Term_Prime():
    global token_index
    if print_switch:
        print("<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>")
    
    update_output(token[token_index], lexeme[token_index], "<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>")

    peek_next_index = token_index
    peek_next_index += 1

    print('700', lexeme[token_index], token[token_index])
    if lexeme[peek_next_index] == '*' or lexeme[peek_next_index] == '/':
        token_index += 2
        print('670', lexeme[token_index], token[token_index])
        Factor()
        Term_Prime()
    elif token[token_index] == "Unknown":
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)
    else:
        Empty()
    
#R27. <Factor> ::= - <Primary> | <Primary>
def Factor():
    global token_index
    if print_switch:
        print("<Factor> ::= - <Primary> | <Primary>")
    update_output(token[token_index], lexeme[token_index], "<Factor> ::= - <Primary> | <Primary>")

    lexer = lexeme[token_index]
    t = token[token_index]
    print('680', lexeme[token_index], token[token_index])
    if lexer == '-':
        token_index += 1
        print('683', lexeme[token_index], token[token_index])
        Primary()
    elif t == 'Identifier' or t == 'Integer' or lexer == '(' or t == 'Real' or lexer == 'true' or lexer == 'false':
        Primary()
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)


#R28. <Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false
def Primary():
    global token_index
    global peek_next_index

    if print_switch:
        print("<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false")
    peek_next_index = token_index
    peek_next_index += 1
    update_output(token[token_index], lexeme[token_index], "<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false")

    print('820', lexeme[token_index], token[token_index])
    if token[token_index] == 'Identifier':
        if lexeme[peek_next_index] == '(':
            token_index += 2
            print('824', lexeme[token_index], token[token_index])
            IDs()
            token_index += 1
            if token[token_index] != ')':
                error_handler(token[token_index],lexeme[token_index], token_index)
                exit(1)
        else:
            return

        #if lexeme[peek_next_index] == '(':
            #token_index += 1
        #else:
            #token_index += 1
            #return
        #print('705', lexeme[token_index], token[token_index])
        #if lexeme[token_index] == '(':
            #token_index += 1
            #IDs()
            #token_index += 1
            #if not lexeme[token_index] == ')':
                #error_handler(token[token_index],lexeme[token_index], token_index)
                #exit(1)
    elif token[token_index] == 'Integer':
        return
    elif lexeme[token_index] == '(':
        token_index += 1
        Expression()
        token_index += 1
        if not lexeme[token_index] == ')':
            error_handler(token[token_index],lexeme[token_index], token_index)
            exit(1)
    elif token[token_index] == 'Real':
        return
    elif lexeme[token_index] == 'true' or lexeme[token_index] == 'false':
        return
    else:
        error_handler(token[token_index],lexeme[token_index], token_index)
        exit(1)


#R29: <Empty> ::= ε
def Empty():
    global token_index
    #token_index += 1
    update_output(token[token_index], lexeme[token_index], "<Empty> ::= ε")

    print('694 Empty:', lexeme[token_index])
    print("<Empty> ::= ε")
    

def main():
    #example()
    Rat24S()
    return 0
            

if __name__ == "__main__":
    main()
