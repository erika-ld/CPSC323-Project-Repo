
def dfsm_int(input):
    states, alphabets = (3,2)
    table = [[0 for i in range(alphabets)] for j in range(states)]
    print("dfsm_int input:", input)
    acceptance_state = True;
    return acceptance_state



def dfsm_real(input):
    states, alphabets = (5,3)
    table = [[0 for i in range(alphabets)] for j in range(states)]
    print("dfsm_real input:", input)
    acceptance_state = True;
    return acceptance_state



def dfsm_id(input):
    states, alphabets = (7,4)
    table = [[0 for i in range(alphabets)] for j in range(states)]
    print("dfsm_id input:", input)
    acceptance_state = True;
    return acceptance_state


def lexer(input):
    #Call the FSMs from this function.

    #Keywords: (14) endif else function integer boolean real if return print scan while endwhile true false
    keywords = ['endif', 'else', 'function', 'integer', 'true', 'false',
                'boolean', 'real', 'if', 'return', 'print', 'scan', 'while', 'endwhile']  
    #Operators: (11) >, <, =, ==, !=, +, -, /, *, <=, >=
    operators = ['>', '<', '=', '==', '!=', '+', '-', '/', '*', '<=', '>=']

    if input in keywords:
        print("Keyword found:", input)
    elif input in operators:
        print("Operator found:", input)
    elif input[0].isalpha():
        # Call DFSM for identifier
        print("Identifier found:", input)
        dfsm_id_output = dfsm_id(input)  
        #Print whether the DFSM_ID found the token to be a valid identifier.
        print(dfsm_id_output)
    elif input[0].isdigit():
        if '.' in input:
            # Call DFSM for real
            print("Real found:", input)
            dfsm_real_output = dfsm_real(input)
            #Print whether the DFSM_REAL found the token to be a valid real.
            print(dfsm_real_output)
        else:
            print("Integer found:", input)
            dfsm_int_output = dfsm_int(input)
            #Print whether the DFSM_INT found the token to be a valid int.
            print(dfsm_int_output)            
    else:
        print("Unknown token:", input)

    return 0


def main():
    # Open file for reading
    with open('test_case_one.txt', 'r') as file:
        contents = file.read()
        if not contents:
            print("File is empty")
            return
        
        token_list = contents.split()
        print("Token list:", token_list)
        for token in token_list:
            lexer(token)

    #Close file_one.

if __name__ == "__main__":
    main()
