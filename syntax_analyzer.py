import lexical


print_switch = True
token_index = 0


#Error handler
def error_handler(token, lexeme, rule):
    print('\nThere is an error on line {0}'.format(rule))
    print('Token: {0}   Lexeme: {1}'.format(token, lexeme))

def update_output(token, lexeme, rule):
    with open('syntax_analyzer', 'a') as file:
        file.write('Token: {0}      Identifier: {1} \n'.format(token, lexeme))
        file.write(rule)

#R1. <Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $
def Rat24S():
    global token_index
    if print_switch:
        print("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")

    if lexical.get_lexeme(token_index) == '$':
        token_index += 1
        if lexical.get_lexeme(token_index) == 'function':
            Optional_Function_Definitions()
            token_index += 1
            if not lexical.get_lexeme(token_index) == '$':
                error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                exit(1)
        elif lexical.get_lexeme(token_index) == 'integer' or lexical.get_lexeme(token_index) == 'boolean' or lexical.get_lexeme(token_index) == 'real':
            Optional_Declaration_List()
            token_index += 1
            if not lexical.get_lexeme(token_index) == '$':
                error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                exit(1)

        Statement_List()
        token_index += 1
        if not lexical.get_lexeme(token_index) == '$':
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)
        
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)

#R2. <Opt Function Definitions> ::= <Function Definitions> | <Empty>
def Optional_Function_Definitions():
    global token_index
    if print_switch:
        print("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")

    if lexical.get_lexeme(token_index) == 'function':
        Function_Definition()
    elif lexical.get_token(token_index) == 'Unknown':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
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

    Function()
    Function_Definition_Prime()

#<Function Definition Prime> ::= <Function Definition> | <Empty>
def Function_Definition_Prime():
    global token_index
    if print_switch:
        print("<Function Definition Prime> ::= <Function Definition> | <Empty>")
    if lexical.get_lexeme(token_index) == 'function':
        Function_Definition()
    elif lexical.get_token(token_index) == 'Unknown':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)
    else:
        Empty()

#R4. <Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>
def Function():
    global token_index
    if print_switch:
        print("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")
    if lexical.get_lexeme(token_index) == 'function':
        token_index += 1
        if lexical.get_token(token_index) == 'Identifier':
            token_index += 1
            if lexical.get_lexeme(token_index) == '(':
                token_index += 1
                Optional_Parameter_List()
                token_index += 1
                if lexical.get_lexeme(token_index) == ')':
                    token_index += 1
                    Optional_Declaration_List()
                    Body()
                    return True
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1) 

#R5. <Opt Parameter List> ::= <Parameter List> | <Empty>
def Optional_Parameter_List():
    global token_index
    if print_switch:
        print("<Opt Parameter List> ::= <Parameter List> | <Empty>")
    
    if lexical.get_token(token_index) == 'Identifier':
        Parameter_List()
    elif lexical.get_token(token_index) == 'Unknown':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)
    else:
        Empty()


#R6. Original: <Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>
#-> Factorized: <Parameter List> ::= <Parameter> <Parameter List Prime>
def Parameter_List():
    global token_index
    if print_switch:
        print("Original: <Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>")
        print("-> Factorized: <Parameter List> ::= <Parameter> <Parameter List Prime>")
    Parameter()
    Parameter_List_Prime()

    error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
    exit(1)


#<Parameter List Prime> ::= <Parameter List> | <Empty> 
def Parameter_List_Prime():
  global token_index
  if print_switch:
    print("<Parameter List Prime> ::= <Parameter List> | <Empty>")

    if lexical.get_token(token_index) == 'Identifier':
        Parameter_List()
    elif lexical.get_token(token_index) == 'Unknown':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)
    else:
        Empty()

#R7. <Parameter> ::= <IDs> <Qualifier>
def Parameter():
    global token_index
    if print_switch:
        print("<Parameter> ::= <IDs> <Qualifier>")

    IDs()
    Qualifier()

    error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
    exit(1)

# R8. <Qualifier> ::= integer | boolean | real
def Qualifier():
    global token_index
    if print_switch:
        print("<Qualifier> ::= integer | boolean | real")
    
    lexeme = lexical.get_lexeme(token_index)
    if lexeme == 'integer' or lexeme == 'boolean' or lexeme == 'real':
        return True
    else:
        print("Error: Expected 'integer', 'boolean', or 'real' in Qualifier")
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)    
        

# R9. <Body> ::= { <Statement List> }
def Body():
    global token_index
    if print_switch:
        print("<Body> ::= { <Statement List> }")
    
    if lexical.get_lexeme(token_index) == '{':
        token_index += 1
        Statement_List()
        token_index += 1
        if not lexical.get_lexeme(token_index) == '}':
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)   
        else:
            return True       


#R10. <Opt Declaration List> ::= <Declaration List> | <Empty>
def Optional_Declaration_List():
    global token_index
    if print_switch:
        print("<Opt Declaration List> ::= <Declaration List> | <Empty>")
    lexeme = lexical.get_lexeme(token_index)
    if lexeme == 'integer' or lexeme == 'boolean' or lexeme == 'real':
        Declaration_List()
    elif lexical.get_token(token_index) == 'Unknown':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)       
    else:
        Empty() 

# R11. <Declaration List> ::= <Declaration> ; <Declaration List Prime>
def Declaration_List():
    global token_index
    if print_switch:
        print("<Declaration List> ::= <Declaration> ; <Declaration List Prime>")
    
    Declaration()
    token_index += 1
    if lexical.get_lexeme(token_index) == ';':
            token_index += 1
            Declaration_List_Prime()
    else:
        print("Missing semicolon (;) after declaration")
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)  

# <Declaration List Prime> ::= <Declaration List> | <Empty>
def Declaration_List_Prime():
    global token_index
    if print_switch:
        print("<Declaration List Prime> ::= <Declaration List> | <Empty>")

    lexeme = lexical.get_lexeme(token_index)
    if lexeme == 'integer' or lexeme == 'boolean' or lexeme == 'real':
        Declaration_List()
    elif lexical.get_token(token_index) == 'Unknown':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)       
    else:
        Empty() 


# R12. <Declaration> ::= <Qualifier> <IDs>
def Declaration():
    global token_index
    if print_switch:
        print("<Declaration> ::= <Qualifier> <IDs>")
    
    Qualifier()
    IDs()

#R13. Original: <IDs> ::= <Identifier> | <Identifier>, <IDs>
#-> Factorized: <IDS> ::= <Identifier> <IDs Prime>
def IDs():
    global token_index
    if print_switch:
        print("Original: <IDs> ::= <Identifier> | <Identifier>, <IDs>")
        print("-> Factorized: <IDS> ::= <Identifier> <IDs Prime>")

    if lexical.get_token(token_index) == 'Identifier':
        IDs_Prime()
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)


#<IDs Prime> ::= , <IDs> | <Empty> 
def IDs_Prime():
    global token_index
    if print_switch:
        print("<IDs Prime> ::= <IDs> | <Empty>")
    if lexical.get_lexeme(token_index) == ',':
        token_index += 1
        IDs()      
    elif lexical.get_token(token_index) == 'Unknown':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
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
    Statement()
    Statement_List_Prime()

#<Statement List Prime> ::= <Statement List> | <Empty>
def Statement_List_Prime():
    global token_index
    if print_switch:
        print("<Statement List Prime> ::= <Statement List> | <Empty>")
    lexeme = lexical.get_lexeme(token_index)
    token = lexical.get_token(token_index)
    if lexeme == '{' or token == 'Identifier' or lexeme == 'if' or lexeme == 'return' or lexeme == 'print' or lexeme == 'scan' or lexeme == 'while':
        Statement_List()
    elif lexical.get_token(token_index) == 'Unknown':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)
    else:
        Empty()

#R15. <Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>
def Statement():
  global token_index
  print("<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>")
  if lexical.get_lexeme(token_index) == '{':
    Compound()
  elif lexical.get_token(token_index) == 'identifier':
    Assign()
  elif lexical.get_lexeme(token_index) == 'if':
    If()
  elif lexical.get_lexeme(token_index) == 'return' :
    Return()
  elif lexical.get_lexeme(token_index) == 'print':
    Print()
  elif lexical.get_lexeme(token_index) == 'scan' :
    Scan()
  elif lexical.get_lexeme(token_index) == 'while':
    While()
  else:
    print("Syntax Error: Invalid statement")
    error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
    exit(1)

#R16. <Compound> ::= { <Statement List> }
def Compound():
    global token_index
    if print_switch:
        print("<Compound> ::= { <Statement List> }")

    if lexical.get_lexeme(token_index) == '{':
        token_index += 1
        Statement_List()
        token_index += 1
        if not lexical.get_lexeme(token_index) == '}':
            print("error in Compound")
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)


#R17. <Assign> ::= <Identifier> = <Expression> ;
def Assign():
    global token_index
    if print_switch:
        print("<Assign> ::= <Identifier> = <Expression> ;")
    
    if lexical.get_token(token_index) == 'Identifier':
        token_index += 1
        if lexical.get_lexeme(token_index) == '=':
            token_index += 1
            Expression()
            token_index += 1
            if not lexical.get_lexeme(token_index) == ';':
                error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                exit(1)


# R18. <If> ::= if ( <Condition> ) <Statement> <If Prime>
def If():
    global token_index
    if print_switch:
        print("<If> ::= if ( <Condition> ) <Statement> <If Prime>")
    
    if lexical.get_lexeme(token_index) == 'if':
        token_index += 1
        if lexical.get_lexeme(token_index) == '(':
            token_index += 1
            Condition()
            token_index += 1
            if lexical.get_lexeme(token_index) == ')':
                token_index += 1
                Statement()
                If_Prime()
            else:
                error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                exit(1)   
        else:
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)

# <If Prime> ::= else <Statement> endif | endif
def If_Prime():
    global token_index
    if print_switch:
        print("<If Prime> ::= else <Statement> endif | endif")
    
    if lexical.get_lexeme(token_index) == 'else':
        token_index += 1
        Statement()
        token_index += 1
        if not lexical.get_lexeme(token_index) == 'endif':
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)
    elif not lexical.get_lexeme(token_index) == 'endif':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)

#R19. <Return> ::= return <Return Prime>
def Return():
    global token_index
    if print_switch:
        print("<Return> ::= return <Return Prime>")
    
    if lexical.get_lexeme(token_index) == 'return':
        token_index += 1
        Return_Prime()
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)

# <Return Prime> ::= <Expression> | <Empty>
def Return_Prime():
    global token_index
    if print_switch:
        print("<Return Prime> ::= <Expression> | <Empty>")
        if not lexical.get_token(token_index) == 'Unknown':
            Expression()
        elif lexical.get_token(token_index) == 'Unknown':
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)
        else:
            Empty()

# R20. <Print> ::= print ( <Expression>);
def Print():
    global token_index
    if print_switch:
        print("<Print> ::= print ( <Expression>);")
    
    if lexical.get_lexeme(token_index) == 'print':
        token_index += 1
        if lexical.get_lexeme(token_index) == '(':
            token_index += 1
            Expression()
            token_index += 1
            if lexical.get_lexeme(token_index) == ')':
                    token_index += 1
                    if not lexical.get_lexeme(token_index) == ';':
                        print("Error: Missing semicolon (;) after print statement")
                        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                        exit(1)
            else:
                error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                exit(1)
        else:
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)       
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)

# R21. <Scan> ::= scan ( <IDs> );
def Scan():
    global token_index
    if print_switch:
        print("<Scan> ::= scan ( <IDs> );")
    
    if lexical.get_lexeme(token_index) == 'scan':
        token_index += 1
        if lexical.get_lexeme(token_index) == '(':
            token_index += 1
            IDs()
            token_index += 1
            if lexical.get_lexeme(token_index) == ')':
                token_index += 1
                if not lexical.get_lexeme(token_index) == ';':
                    error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                    exit(1)
                else:
                    error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                    exit(1)
            else:
                error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                exit(1)
        else:
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)

# R22. <While> ::= while ( <Condition> ) <Statement> endwhile
def While():
    global token_index
    if print_switch:
        print("<While> ::= while ( <Condition> ) <Statement> endwhile")
    if lexical.get_lexeme(token_index) == 'while':
        token_index += 1
        if lexical.get_lexeme(token_index) == '(':
            token_index += 1
            Condition()
            token_index += 1
            if lexical.get_lexeme(token_index) == ')':
                token += 1
                Statement()
                if not lexical.get_lexeme(token_index) == 'endwhile':
                    error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                    exit(1)
            else:
                error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                exit(1)
        else:
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)

            

#R23. <Condition> ::= <Expression> <Relop> <Expression>
def Condition():
    global token_index
    if print_switch:
        print("<Condition> ::= <Expression> <Relop> <Expression>")
    
    Expression()
    Relop()
    Expression()

#R24. <Relop> ::= == | != | > | < | <= | =>
def Relop():
    global token_index
    if print_switch:
        print("<Relop> ::= == | != | > | < | <= | =>")

    if not lexical.get_lexeme(token_index) == '==' or lexical.get_lexeme(token_index) == '!=' or lexical.get_lexeme(token_index) == '>' or lexical.get_lexeme(token_index) == '<' or lexical.get_lexeme(token_index) == '<=' or lexical.get_lexeme(token_index) == '>=':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)

# R25. <Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>
# Revised: <Expression> ::= <Term> <Expression_Prime>
def Expression():
    global token_index
    if print_switch:
        print("<Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>")
        print("Revised: <Expression> ::= <Term> <Expression_Prime>")  
    
    Term()
    Expression_Prime()

#<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>
def Expression_Prime():
    global token_index
    if print_switch:
        print("<Expression Prime> ::= + <Term> <Expression Prime> | - <Term> <Expression Prime> | <Empty>")
    
    lexer = lexical.get_lexeme(token_index)
    if lexer == '+' or lexer == '-':
        token_index += 1
        Term()
        Expression_Prime()
    elif lexical.get_token(token_index) == 'Unknown':
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
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

    Factor()
    Term_Prime()

#<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>
def Term_Prime():
    global token_index
    if print_switch:
        print("<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>")

    if lexical.get_lexeme(token_index) == '*' or lexical.get_lexeme(token_index) == '/':
        token_index += 1
        Factor()
        Term_Prime()
    elif lexical.get_token(token_index) == "Unknown":
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)
    else:
        Empty()
    
#R27. <Factor> ::= - <Primary> | <Primary>
def Factor():
    global token_index
    if print_switch:
        print("<Factor> ::= - <Primary> | <Primary>")

    lexer = lexical.get_lexeme(token_index)
    token = lexical.get_token(token_index)
    if lexer == '-':
        token_index += 1
        Primary()
    elif token == 'Identifier' or token == 'Integer' or lexeme == '(' or token == 'Real' or lexeme == 'true' or lexeme == 'false':
        Primary()
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)


#R28. <Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false
def Primary():
    global token_index
    if print_switch:
        print("<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false")
    if lexical.get_token(token_index) == 'Identifier':
        token_index += 1
        if lexical.get_lexeme(token_index) == '(':
            token_index += 1
            IDs()
            token_index += 1
            if not lexical.get_lexeme(token_index) == ')':
                error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
                exit(1)
    elif lexical.get_token(token_index) == 'Integer':
        return True
    elif lexical.get_lexeme(token_index) == '(':
        token_index += 1
        Expression()
        token_index += 1
        if not lexical.get_lexeme(token_index) == ')':
            error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
            exit(1)
    elif lexical.get_token(token_index) == 'Real':
        return True
    elif lexical.get_lexeme(token_index) == 'true' or lexical.get_lexeme(token_index) == 'false':
        return True
    else:
        error_handler(lexical.get_token(token_index),lexical.get_lexeme(token_index), token_index)
        exit(1)


#R29: <Empty> ::= ε
def Empty():
    global token_index
    print("<Empty> ::= ε")
    

def main():
    #example()
    Rat24S()
    return 0
            

if __name__ == "__main__":
    main()
