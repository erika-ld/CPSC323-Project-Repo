
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

    return 1


def lexer(input):
    #Call the FSMs from this function.

    while True:
        #endif else function integer boolean real if return print scan while endwhile true false
        if input == ('endif' or 'else' or 'function' or 'integer' or 
        'boolean' or 'real' or 'if' or 'return' or 'print' or 'scan' or 'while' or 'endwhile'):
            #process keyword
            return 1
        elif input[0].isalpha():
            #Call DFSM Id
            print(input[0])
            dfsm_id_output = dfsm_id()
        else:
            break
    
    return 1


def main():
    
    #Open file_one (test_case_one.txt) for reading purposes.
    file_one = open('test_case_one.txt')
    contents = file_one.read()
    token_list = contents.split()
    print(token_list)
    for i in token_list:
        lexer(i)
    #Need help implementing while loop to reach end of file.

    #Close file_one.
    file_one.close()

    #print(lexer())

if __name__ == "__main__":
    main()
