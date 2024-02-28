
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
        char = input.read(1)          
        #Terminates when whitespace is reached.
        if char.isalpha():
            print(char)
            #Call DFSM Id
        else:
            break
    
    return 1


def main():
    
    #Open file_one (test_case_one.txt) for reading purposes.
    file_one = open('test_case_one.txt' , 'r')
    lexer(file_one)
    #Need help implementing while loop to reach end of file.

    #Close file_one.
    file_one.close()

    #print(lexer())

if __name__ == "__main__":
    main()
