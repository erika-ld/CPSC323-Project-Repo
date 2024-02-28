
def dfsm_int(input):
    states, alphabets = (3,2)
    table = [[0 for i in range(alphabets)] for j in range(states)]
    print(table)
    return 1
dfsm_int(12)


def dfsm_real(input):
    states, alphabets = (5,3)
    table = [[0 for i in range(alphabets)] for j in range(states)]
    print(table)
    return 1

dfsm_real(12)

def dfsm_id(input):
    states, alphabets = (7,4)
    table = [[0 for i in range(alphabets)] for j in range(states)]
    print(table)
    return 1

dfsm_id(12)

def lexer():
    return 1

def main():
    print(lexer())

if __name__ == "__main__":
    main()
