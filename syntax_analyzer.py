import lexical

#36-37 functions for each non-terminal 

print_switch = True

#def print_file(token, lexemes, production_rules):
    #with open(syntax_output_file, 'w') as output:
        #output.write("Test")


#R1. <Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $
def Rat24S():
    if print_switch:
        print("<Rat24S> ::= $ <Opt Function Definitions> $ <Opt Declaration List> $ <Statement List> $")
    
#R2. <Opt Function Definitions> ::= <Function Definitions> | <Empty>
def Optional_Function_Definitions():
    if print_switch:
        print("<Opt Function Definitions> ::= <Function Definitions> | <Empty>")

#R3. Original: <Function Definitions> ::= <Function> | <Function> <Function Definitions>    
#Factorized: <Function Definition> ::= <Function> <Function Definition Prime>
def Function_Definition():
    if print_switch:
        print("Original: <Function Definitions> ::= <Function> | <Function> <Function Definitions>")
        print("Factorized: <Function Definition> ::= <Function> <Function Definition Prime>")

#<Function Definition Prime> ::= <Function Definition> | <Empty>
def Function_Definition_Prime():
    if print_switch:
        print("<Function Definition Prime> ::= <Function Definition> | <Empty>")

#R4. <Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>
def Function():
    if print_switch:
        print("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")

#R5. <Opt Parameter List> ::= <Parameter List> | <Empty>
def Optional_Parameter_List():
    if print_switch:
        print("<Opt Parameter List> ::= <Parameter List> | <Empty>")

#R6. Original: <Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>
#Factorized: <Parameter List> ::= <Parameter> <Parameter List Prime>
def Parameter_List():
    if print_switch:
        print("Original: <Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>")
        print("Factorized: <Parameter List> ::= <Parameter> <Parameter List Prime>")

#<Parameter List Prime> ::= <Parameter List> | <Empty> 
def Parameter_List_Prime():
    if print_switch:
        print("<Parameter List Prime> ::= <Parameter List> | <Empty>")

#R7. <Parameter> ::= <IDs > <Qualifier>
def Parameter():
    if print_switch:
        print("[<Parameter> ::= <IDs > <Qualifier>")

#R8. <Qualifier> ::= integer | boolean | real
def Qualifier():
    if print_switch:
        print("<Qualifier> ::= integer | boolean | real")

#R9. <Body> ::= { < Statement List> }
def Body():
    if print_switch:
        print("<Body> ::= { < Statement List> }")

#R10. <Opt Declaration List> ::= <Declaration List> | <Empty>
def Optional_Declaration_List():
    if print_switch:
        print("<Opt Declaration List> ::= <Declaration List> | <Empty>")     

#R11. Original: <Declaration List> ::= <Declaration> ; | <Declaration> ; <Declaration List>
#Factorized: <Declaration List> ::= <Declaration> ; <Declaration List Prime>
def Declaration_List():
    if print_switch:
        print("Original: <Declaration List> := <Declaration> ; | <Declaration> ; <Declaration List>")
        print("Factorized: <Declaration List> ::= <Declaration> ; <Declaration List Prime>")

#<Declaration List Prime> ::= <Declaration List> | <Empty>
def Declaration_List_Prime():
    if print_switch:
        print("<Declaration List Prime> ::= <Declaration List> | <Empty>")

#R12. <Declaration> ::= <Qualifier > <IDs>
def Declaration():
    if print_switch:
        print("<Declaration> ::= <Qualifier > <IDs>")

#R13. Original: <IDs> ::= <Identifier> | <Identifier>, <IDs>
#Factorized: <IDS> ::= <Identifier> <IDs Prime>
def IDs():
    if print_switch:
        print("Original: <IDs> ::= <Identifier> | <Identifier>, <IDs>")
        print("Factorized: <IDS> ::= <Identifier> <IDs Prime>")

#<IDs Prime> ::= <IDs> | <Empty> 
def IDs_Prime():
    if print_switch:
        print("<IDs Prime> ::= <IDs> | <Empty>")

#R14. Original: <Statement List> ::= <Statement> | <Statement> <Statement List>
#Factorized: <Statement List> ::= <Statement> <Statement List Prime>
def Statement_List():
    if print_switch:
        print("Original: <Statement List> ::= <Statement> | <Statement> <Statement List>")
        print("Factorized: <Statement List> ::= <Statement> <Statement List Prime>")

#<Statement List Prime> ::= <Statement List> | <Empty>
def Statement_List_Prime():
    if print_switch:
        print("<Statement List Prime> ::= <Statement List> | <Empty>")

#R15. <Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>
def Statement():
    if print_switch:
        print("<Statement> ::= <Compound> | <Assign> | <If> | <Return> | <Print> | <Scan> | <While>")

#R16. <Compound> ::= { <Statement List> }
def Compound():
    if print_switch:
        print("<Compound> ::= { <Statement List> }")

#R17. <Assign> ::= <Identifier> = <Expression> ;
def Assign():
    if print_switch:
        print("<Assign> ::= <Identifier> = <Expression> ;")

#R18. Original: <If> ::= if ( <Condition> ) <Statement> endif | if ( <Condition> ) <Statement> else <Statement> endif
#Factorized: <If> ::= if ( <Condition> ) <Statement> <If Prime>
def If():
    if print_switch:
        print("Original: <If> ::= if ( <Condition> ) <Statement> endif |if ( <Condition> ) <Statement> else <Statement> endif")
        print("Factorized: <If> ::= if ( <Condition> ) <Statement> <If Prime>")

#<If Prime> ::= else <Statement> endif | endif
def If_Prime():
    if print_switch:
        print("<If Prime> ::= else <Statement> endif | endif")

#R19. Original: <Return> ::= return ; | return <Expression> ;
#Factorized: <Return> ::= return <Return Prime>
def Return():
    if print_switch:
        print("Original: <Return> ::= return ; | return <Expression> ;")
        print("Factorized: <Return> ::= return <Return Prime>")

#<Return Prime> ::= <Expression> | <Empty>
def Return_Prime():
    if print_switch:
        print("<Return Prime> ::= <Expression> | <Empty>")

#R20. <Print> ::= print ( <Expression>);
def Print():
    if print_switch:
        print("<Print> ::= print ( <Expression>);")

#R21. <Scan> ::= scan ( <IDs> );
def Scan():
    if print_switch:
        print("<Scan> ::= scan ( <IDs> );")

#R22. <While> ::= while ( <Condition> ) <Statement> endwhile
def While():
    if print_switch:
        print("<While> ::= while ( <Condition> ) <Statement> endwhile")

#R23. <Condition> ::= <Expression> <Relop> <Expression>
def Condition():
    if print_switch:
        print("<Condition> ::= <Expression> <Relop> <Expression>")

#R24. <Relop> ::= == | != | > | < | <= | =>
def Relop():
    if print_switch:
        print("<Relop> ::= == | != | > | < | <= | =>")

#R25. <Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>
def Expression():
  global token_index 
  if print_switch:
    print("<Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>")
    print("Revised: <Expression> ::= <Term> <Expression_Prime>")  
  # Parse the first term
  Term()

   # Check if the next token is either '+' or '-'
  if lexical.get_lexeme(token_index) == '+' or lexical.get_lexeme(token_index) == '-':
        # Move to the next token
        token_index += 1
        # Parse the next term
        Term()

def Expression_Prime():
    if print_switch:
        print("[Rule]")

#R26. Original: <Term> ::= <Term> * <Factor> | <Term> / <Factor> | <Factor>
#Revised: <Term> ::= <Factor> <Term Prime>
def Term():
    if print_switch:
        print("Original: <Term> ::= <Term> * <Factor> | <Term> / <Factor> | <Factor>")
        print("Revised: <Term> ::= <Factor> <Term Prime>")

def Term_Prime():
    if print_switch:
        print("<Term Prime> ::= * <Factor> <Term Prime> | / <Factor> <Term Prime> | <Empty> ")

#R27. <Factor> ::= - <Primary> | <Primary>
def Factor():
    if print_switch:
        print("<Factor> ::= - <Primary> | <Primary>")

#R28. <Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false
def Primary():
    if print_switch:
        print("<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false")


def main():
    return 0
            

if __name__ == "__main__":
    main()