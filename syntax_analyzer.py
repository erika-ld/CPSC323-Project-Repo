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

#R3. <Function Definitions> ::= <Function> | <Function> <Function Definitions>    
def Function_Definition():
    if print_switch:
        print("<Function Definitions> ::= <Function> | <Function> <Function Definitions>  ")
#R4. <Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>
def Function():
    if print_switch:
        print("<Function> ::= function <Identifier> ( <Opt Parameter List> ) <Opt Declaration List> <Body>")

#R5. <Opt Parameter List> ::= <Parameter List> | <Empty>
def Optional_Parameter_List():
    if print_switch:
        print("<Opt Parameter List> ::= <Parameter List> | <Empty>")

#R6. <Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>
def Parameter_List():
    if print_switch:
        print("<Parameter List> ::= <Parameter> | <Parameter> , <Parameter List>")

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

#R11. <Declaration List> := <Declaration> ; | <Declaration> ; <Declaration List>
def Declaration_List():
    if print_switch:
        print("<Declaration List> := <Declaration> ; | <Declaration> ; <Declaration List>")

#R12. <Declaration> ::= <Qualifier > <IDs>
def Declaration():
    if print_switch:
        print("<Declaration> ::= <Qualifier > <IDs>")

#R13. <IDs> ::= <Identifier> | <Identifier>, <IDs>
def IDs():
    if print_switch:
        print("<IDs> ::= <Identifier> | <Identifier>, <IDs>")

#R14. <Statement List> ::= <Statement> | <Statement> <Statement List>
def Statement_List():
    if print_switch:
        print("<Statement List> ::= <Statement> | <Statement> <Statement List>")

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

#R18. <If> ::= if ( <Condition> ) <Statement> endif |if ( <Condition> ) <Statement> else <Statement> endif
def If():
    if print_switch:
        print("<If> ::= if ( <Condition> ) <Statement> endif |if ( <Condition> ) <Statement> else <Statement> endif")

#R19. <Return> ::= return ; | return <Expression> ;
def Return():
    if print_switch:
        print("<Return> ::= return ; | return <Expression> ;")

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
    if print_switch:
        print("<Expression> ::= <Expression> + <Term> | <Expression> - <Term> | <Term>")

#R26. <Term> ::= <Term> * <Factor> | <Term> / <Factor> | <Factor>
def Term():
    if print_switch:
        print("<Term> ::= <Term> * <Factor> | <Term> / <Factor> | <Factor>")

#R27. <Factor> ::= - <Primary> | <Primary>
def Factor():
    if print_switch:
        print("<Factor> ::= - <Primary> | <Primary>")

#R28. <Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false
def Primary():
    if print_switch:
        print("<Primary> ::= <Identifier> | <Integer> | <Identifier> ( <IDs> ) | ( <Expression> ) | <Real> | true | false")

def If_Prime():
    if print_switch:
        print("[Rule]")

def Expression_Prime():
    if print_switch:
        print("[Rule]")

def Term_Prime():
    if print_switch:
        print("[Rule]")

def Function_Definition_Prime():
    if print_switch:
        print("")

def Parameter_List_Prime():
    if print_switch:
        print("")

def Declaration_List_Prime():
    if print_switch:
        print("")

def IDs_Prime():
    if print_switch:
        print("")

def Statement_List_Prime():
    if print_switch:
        print("")

def Return_Prime():
    if print_switch:
        print("")



def main():
    return 0
            

if __name__ == "__main__":
    main()