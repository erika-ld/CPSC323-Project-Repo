
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


def lexer():
    return 1

def main():
    
    #Open file_one (test_case_one.txt) for reading purposes.
    file_one = open('test_case_one.txt' , 'r')

    #While loop to read characters from file_one.
    while True:
        char = file_one.read(1)          
        if not char: 
            break
        print(char)

    #Close file_one.
    file_one.close()

    print(lexer())

if __name__ == "__main__":
    main()
