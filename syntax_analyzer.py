import lexical

print_switch = True
token_index = 0

#Error handler
def error_handler(token, lexeme):
    print('\nThere is an error on line {0}'.format(token_index))
    print('Token: {0}, Lexeme: {1}'.format(token, lexeme))

def update_output(token, lexeme, rule):
    with open('syntax_analyzer', 'a') as file:
        file.write('Token: {0}      Identifier: {1} \n'.format(token, lexeme))
        file.write(rule)

def example():
    ex = 'hello'
    ex2 = 'example'
    error_handler(ex, ex2)

#R1. <Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $
def Rat24S():
    if print_switch:
        print("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")

    if lexical.get_lexeme(token_index) == '$':
        token_index += 1
        if Optional_Function_Definitions():
            token_index += 1
            if not lexical.get_lexeme(token_index) == '$':
                print("error")
                exit(1)
        elif Optional_Declaration_List():
            token_index += 1
            if not lexical.get_lexeme(token_index) == '$':
                print("error")
                exit(1)

        token_index += 1
        Statement_List()
        token_index += 1
        if not lexical.get_lexeme(token_index) == '$':
            print("error")
            exit(1)
        
        return True
    else:
        print("error")
        exit(1)

#R2. <Opt Function Definitions> ::= <Function Definitions> | <Empty>
def Optional_Function_Definitions():
    if print_switch:
        print("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")

    if Function_Definition() | Empty():
        return True
    else:
        print("error")
        exit(1)

#R3. Original: <Function Definitions> ::= <Function> | <Function> <Function Definitions>
#Factorized: <Function Definition> ::= <Function> <Function Definition Prime>
def Function_Definition():
    if print_switch:
        print("Original: <Function Definitions> ::= <Function> | <Function> <Function Definitions>")
        print("Factorized: <Function Definition> ::= <Function> <Function Definition Prime>")

    if Function():
        token_index += 1
        if Function_Definition_Prime():
            return True
        else:
            print("error")
            exit(1)
    else:
        print("error")
        exit(1)

#<Function Definition Prime> ::= <Function Definition> | <Empty>
def Function_Definition_Prime():
    if print_switch:
        print("<Function Definition Prime> ::= <Function Definition> | <Empty>")
    if Function_Definition() | Empty():
      return True
    else:
        print("error")
        exit(1)

#R4. <Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>
def Function():
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
                    token_index += 1
                    Body()
                    return True
                else:
                    print("error")
            print("error")
        print("error")
    else:
        print("error")
        exit(1) 

#R5. <Opt Parameter List> ::= <Parameter List> | <Empty>
def Optional_Parameter_List():
    if print_switch:
        print("<Opt Parameter List> ::= <Parameter List> | <Empty>")
    if Parameter_List() or Empty():
        return True
    else:
        print("error")
        exit(1)

#R6. Original: <Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>
#Factorized: <Parameter List> ::= <Parameter> <Parameter List Prime>
def Parameter_List():
    if print_switch:
        print("Original: <Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>")
        print("Factorized: <Parameter List> ::= <Parameter> <Parameter List Prime>")
    if Parameter():
        token_index += 1
        if Parameter_List_Prime():
            return True
        else:
            print("error")
            exit(1)
    else:
        print('error')
        exit(1)


#<Parameter List Prime> ::= <Parameter List> | <Empty> 
def Parameter_List_Prime():
  if print_switch:
    print("<Parameter List Prime> ::= <Parameter List> | <Empty>")

    if Parameter_List() or Empty():
        return True
    else:
        print('error')
        exit(1)

#R7. <Parameter> ::= <IDs> <Qualifier>
def Parameter():
    if print_switch:
        print("<Parameter> ::= <IDs > <Qualifier>")

    if IDs():
        token_index += 1
        if Qualifier():
            return True
        else:
            print("error")
            exit(1)
    else:
        print("error")
        exit(1)

# R8. <Qualifier> ::= integer | boolean | real
def Qualifier():
    if print_switch:
        print("<Qualifier> ::= integer | boolean | real")
    
    lexeme = lexical.get_lexeme(token_index)
    if lexeme == 'integer' or lexeme == 'boolean' or lexeme == 'real':
        #need this?
        token_index += 1
        return True
    else:
        print("Error: Expected 'integer', 'boolean', or 'real' in Qualifier")
        return False


# R9. <Body> ::= { <Statement List> }
def Body():
    if print_switch:
        print("<Body> ::= { <Statement List> }")
    
    if lexical.get_lexeme(token_index) == '{':
        token_index += 1
        if Statement_List():
            if lexical.get_lexeme(token_index) == '}':
                token_index += 1
                return True
            else:
                print("Error: Missing '}' in Body")
                return False
        else:
            print("Error: Problem parsing Statement List in Body")
            return False
    else:
        print("Error: Missing '{' in Body")
        return False


#R10. <Opt Declaration List> ::= <Declaration List> | <Empty>
def Optional_Declaration_List():
    if print_switch:
        print("<Opt Declaration List> ::= <Declaration List> | <Empty>")
    if Declaration_List() | Empty():
        return True
    else:
        print("error")
        exit(1)    

# R11. <Declaration List> ::= <Declaration> ; <Declaration List Prime>
def Declaration_List():
    if print_switch:
        print("<Declaration List> ::= <Declaration> ; <Declaration List Prime>")
    
    if Declaration():
        token_index += 1
        if lexical.get_lexeme(token_index) == ';':
            token_index += 1
            return Declaration_List_Prime()
        else:
            print("Missing semicolon (;) after declaration")
            return False
    else:
        print("Error in declaration")
        return False

# <Declaration List Prime> ::= <Declaration List> | <Empty>
def Declaration_List_Prime():
    if print_switch:
        print("<Declaration List Prime> ::= <Declaration List> | <Empty>")
    
    if Declaration_List():
        return True
    else:
        Empty()
        return True

# R12. <Declaration> ::= <Qualifier> <IDs>
def Declaration():
    if print_switch:
        print("<Declaration> ::= <Qualifier> <IDs>")
    
    if Qualifier():
        if IDs():
            return True
        else:
            print("Error: Invalid IDs in Declaration")
            return False
    else:
        print("Error: Invalid Qualifier in Declaration")
        return False

#R13. Original: <IDs> ::= <Identifier> | <Identifier>, <IDs>
#Factorized: <IDS> ::= <Identifier> <IDs Prime>
def IDs():
    if print_switch:
        print("Original: <IDs> ::= <Identifier> | <Identifier>, <IDs>")
        print("Factorized: <IDS> ::= <Identifier> <IDs Prime>")

    if lexical.get_token(token_index) == 'Identifier':
        if IDs_Prime():
            return True
        else:
            print("error")
            exit(1)
    else:
        print("error")
        exit(1)

#<IDs Prime> ::= , <IDs> | <Empty> 
def IDs_Prime():
    if print_switch:
        print("<IDs Prime> ::= <IDs> | <Empty>")
    if lexical.get_lexeme(token_index) == ',':
        token_index += 1
        if IDs():
            return True
        else:
            print("error")
            exit(1)
    elif Empty():
        return True
    else:
        print("error")
        exit(1)

#R14. Original: <Statement List> ::= <Statement> | <Statement> <Statement List>
#Factorized: <Statement List> ::= <Statement> <Statement List Prime>
def Statement_List():
    if print_switch:
        print("Original: <Statement List> ::= <Statement> | <Statement> <Statement List>")
        print("Factorized: <Statement List> ::= <Statement> <Statement List Prime>")
    if Statement():
        if Statement_List_Prime():
            return True
        else:
            print("error")
            exit(1)
    else:
        print("error")
        exit(1)

#<Statement List Prime> ::= <Statement List> | <Empty>
def Statement_List_Prime():
    if print_switch:
        print("<Statement List Prime> ::= <Statement List> | <Empty>")
    if Statement_List() | Empty():
        return True
    else:
        print("error")
        exit(1)

#R15. <Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>
def Statement(self):
  print("<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>")
  if lexical.tokens[0].get_lexeme == '{':
    if Compound() is True:
      return True
  elif lexical.tokens[0].get_token == 'identifier':
    if Assign() is True: 
        return True
  elif lexical.tokens[0].get_lexeme == 'if':
    if If() is True:
        return True
  elif lexical.tokens[0].get_lexeme == 'return' :
    if Return() is True:
        return True
  elif lexical.tokens[0].get_lexeme == 'print':
    if Print() is True:
        return True
  elif lexical.tokens[0].get_lexeme == 'scan' :
    if Scan() is True:
        return True
  elif lexical.tokens[0].get_lexeme == 'while':
    if While() is True:
        return True
  else:
    print("Syntax Error: Invalid statement")
    return False

#R16. <Compound> ::= { <Statement List> }
def Compound():
  if print_switch:
    print("<Compound> ::= { <Statement List> }")
    if (
        lexical.get_token(token_index - 1) == '{' and 
        lexical.get_token(token_index) == 'Identifier' and 
        lexical.get_token(token_index + 1) == '}'
    ):
      return True
    else:
      print("error in Compound")
      exit(1)

#R17. <Assign> ::= <Identifier> = <Expression> ;
def Assign():
    if print_switch:
        print("<Assign> ::= <Identifier> = <Expression> ;")
    if (
      lexical.get_token(token_index - 1) == '=' and 
      lexical.get_token(token_index) == 'Identifier' and 
      lexical.get_token(token_index + 1) == ';'
    ):
      return True
    else:
      print("error")
      exit(1)

# R18. <If> ::= if ( <Condition> ) <Statement> <If Prime>
def If():
    if print_switch:
        print("<If> ::= if ( <Condition> ) <Statement> <If Prime>")
    
    if lexical.get_lexeme(token_index) == 'if':
        token_index += 1
        if lexical.get_lexeme(token_index) == '(':
            token_index += 1
            if Condition():
                if lexical.get_lexeme(token_index) == ')':
                    token_index += 1
                    if Statement():
                        return If_Prime()
                    else:
                        print("Error: Invalid statement in if branch")
                        return False
                else:
                    print("Error: Missing closing parenthesis ')' in if statement")
                    return False
            else:
                print("Error: Invalid condition in if statement")
                return False
        else:
            print("Error: Missing opening parenthesis '(' in if statement")
            return False
    else:
        print("Error: 'if' keyword expected")
        return False

# <If Prime> ::= else <Statement> endif | endif
def If_Prime():
    if print_switch:
        print("<If Prime> ::= else <Statement> endif | endif")
    
    if lexical.get_lexeme(token_index) == 'else':
        token_index += 1
        if Statement():
            if lexical.get_lexeme(token_index) == 'endif':
                token_index += 1
                return True
            else:
                print("Error: 'endif' keyword expected after else branch in if statement")
                return False
        else:
            print("Error: Invalid statement in else branch of if statement")
            return False
    elif lexical.get_lexeme(token_index) == 'endif':
        token_index += 1
        return True
    else:
        print("Error: 'else' or 'endif' keyword expected")
        return False

#R19. <Return> ::= return <Return Prime>
def Return():
    if print_switch:
        print("<Return> ::= return <Return Prime>")
    
    if lexical.get_lexeme(token_index) == 'return':
        token_index += 1
        return Return_Prime()
    else:
        print("Error: 'return' keyword expected")
        return False

# <Return Prime> ::= <Expression> | <Empty>
def Return_Prime():
    if print_switch:
        print("<Return Prime> ::= <Expression> | <Empty>")
    
    if lexical.get_lexeme(token_index) == ';':
        token_index += 1
        return True
    elif Expression():
        return True
    else:
        Empty()
        return True

# R20. <Print> ::= print ( <Expression>);
def Print():
    if print_switch:
        print("<Print> ::= print ( <Expression>);")
    
    if lexical.get_lexeme(token_index) == 'print':
        token_index += 1
        if lexical.get_lexeme(token_index) == '(':
            token_index += 1
            if Expression():
                if lexical.get_lexeme(token_index) == ')':
                    token_index += 1
                    if lexical.get_lexeme(token_index) == ';':
                        token_index += 1
                        return True
                    else:
                        print("Error: Missing semicolon (;) after print statement")
                        return False
                else:
                    print("Error: Missing closing parenthesis ')' in print statement")
                    return False
            else:
                print("Error: Invalid expression in print statement")
                return False
        else:
            print("Error: Missing opening parenthesis '(' in print statement")
            return False
    else:
        print("Error: 'print' keyword expected")
        return False

# R21. <Scan> ::= scan ( <IDs> );
def Scan():
    if print_switch:
        print("<Scan> ::= scan ( <IDs> );")
    
    if lexical.get_lexeme(token_index) == 'scan':
        token_index += 1
        if lexical.get_lexeme(token_index) == '(':
            token_index += 1
            if IDs():
                if lexical.get_lexeme(token_index) == ')':
                    token_index += 1
                    if lexical.get_lexeme(token_index) == ';':
                        token_index += 1
                        return True
                    else:
                        print("Error: Missing semicolon (;) after scan statement")
                        return False
                else:
                    print("Error: Missing closing parenthesis ')' in scan statement")
                    return False
            else:
                print("Error: Invalid IDs in scan statement")
                return False
        else:
            print("Error: Missing opening parenthesis '(' in scan statement")
            return False
    else:
        print("Error: 'scan' keyword expected")
        return False

# R22. <While> ::= while ( <Condition> ) <Statement> endwhile
def While():
    if print_switch:
        print("<While> ::= while ( <Condition> ) <Statement> endwhile")
    if lexical.get_lexeme(token_index) == 'while':
        token_index += 1
        if lexical.get_lexeme(token_index) == '(':
            token_index += 1
            if Condition():
                token_index += 1
                if lexical.get_lexeme(token_index) == ')':
                    return True
                else:
                    print("error")
                    return False
            else:
                print("error")
                return False
        else:
            print("error")
            return False
    else:
        print("error")
        return False

#R23. <Condition> ::= <Expression> <Relop> <Expression>
def Condition():
    if print_switch:
        print("<Condition> ::= <Expression> <Relop> <Expression>")
    
    if Expression():
        if Relop():
            if Expression():
                return True
            else:
                return False
                print("error")
        else:
            return False
            print("error")
    else:
        return False

#R24. <Relop> ::= == | != | > | < | <= | =>
def Relop():
    if print_switch:
        print("<Relop> ::= == | != | > | < | <= | =>")
    if lexical.get_lexeme(token_index) == '==' or lexical.get_lexeme(token_index) == '!=' or lexical.get_lexeme(token_index) == '>' or lexical.get_lexeme(token_index) == '<' or lexical.get_lexeme(token_index) == '<=' or lexical.get_lexeme(token_index) == '>=':
        return True
    else:
        return False

# R25. <Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>
def Expression():
    global token_index 
    if print_switch:
        print("<Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>")
        print("Revised: <Expression> ::= <Term> <Expression_Prime>")  
    
    if not Term():
        return False

    # Check if there's an expression prime part
    if not Expression_Prime():
        return False

    # Check if the next token is either '+' or '-'
    while lexical.get_lexeme(token_index) == '+' or lexical.get_lexeme(token_index) == '-':
        # Move to the next token
        token_index += 1
        # Parse the next term
        if not Term():
            return False

    return True

def Expression_Prime():
    if print_switch:
        print("[Rule]")
    
    # Logic for expression prime, if any, can be added here
    return True  # Placeholder logic, modify as needed


#R26. Original: <Term> ::= <Term> * <Factor> | <Term> / <Factor> | <Factor>
#Revised: <Term> ::= <Factor> <Term Prime>
def Term():
    if print_switch:
        print("Original: <Term> ::= <Term> * <Factor> | <Term> / <Factor> | <Factor>")
        print("Revised: <Term> ::= <Factor> <Term Prime>")
    if Factor():
        if Term_Prime():
            return True
    
    return False

#<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>
def Term_Prime():
    if print_switch:
        print("<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty>")

    if lexical.get_lexeme(token_index) == '*' or lexical.get_lexeme(token_index) == '/':
        token_index += 1
        if Factor():
            return Term_Prime()
    elif lexical.get_(token_index) == "Unknown":
        #report error
        print("error")
        return False
    else:
        Empty()
        return True
    
#R27. <Factor> ::= - <Primary> | <Primary>
def Factor():
    if print_switch:
        print("<Factor> ::= - <Primary> | <Primary>")
    if lexical.get_lexeme(token_index) == '-':
        token_index += 1
        return Primary()
    else:
        return Primary()


#R28. <Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false
def Primary():
    if print_switch:
        print("<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false")
    if lexical.get_token(token_index) == 'Identifier':
        token_index += 1
        if lexical.get_lexeme(token_index) == '[':
            token_index += 1
            if IDs():
                token_index += 1
                return lexical.get_lexeme(token_index) == ']'
        else:
            return True
    elif lexical.get_token(token_index) == 'Integer':
        return True
    elif lexical.get_lexeme(token_index) == '(':
        token_index += 1
        if Expression(): 
            token_index += 1
            if lexical.get_lexeme(token_index) == ')':
                return True
            else:
                return False
                print("error")
        else:
            return False
            print("error")
    elif lexical.get_token(token_index) == 'Real':
        return True
    elif lexical.get_lexeme(token_index) == 'true' or lexical.get_lexeme(token_index) == 'false':
        return True
    else:
        return False


#R29: <Empty> ::= ε
def Empty():
    print("<Empty> ::= ε")
    

def main():
    #example()
    print(lexical.get_token(0))

    #Rat24S()
    return 0
            

if __name__ == "__main__":
    main()
