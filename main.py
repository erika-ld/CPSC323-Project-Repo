
def dfsm_int(input):
    states, alphabets = (3,2)
    table = [[0 for i in range(alphabets)] for j in range(states)]
    print(table)
    return 1



def dfsm_real(input):
    states, alphabets = (5,3)
    table = [[0 for i in range(alphabets)] for j in range(states)]
    print(table)
    return 1



def dfsm_id(input):
    states, alphabets = (7,4)
    table = [[0 for i in range(alphabets)] for j in range(states)]
    print(table)


def lexer(input):
    #Call the FSMs from this function.

    #Keywords: (14) endif else function integer boolean real if return print scan while endwhile true false
   
    keywords = ['endif', 'else', 'function', 'integer', 'true', 'false',
                'boolean', 'real', 'if', 'return', 'print', 'scan', 'while', 'endwhile']    
    if input in keywords:
        # Process keyword
        print("Keyword found:", input)
    elif input[0].isalpha():
        # Call DFSM for identifier
        print("Identifier found:", input)
        # dfsm_id_output = dfsm_id(input)  # Call your identifier FSM here
    else:
        print("Unknown token:", input)

    return 0


def main():
    
    #Open file_one (test_case_one.txt) for reading purposes.
    file_one = open('test_case_one.txt')
    contents = file_one.read()
    token_list = contents.split()
    print(token_list)
    for i in token_list:
        lexer(i)

    #Close file_one.
    file_one.close()

if __name__ == "__main__":
    main()
