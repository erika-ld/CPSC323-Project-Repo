keywords = ['endif', 'else', 'function', 'integer', 'true', 'false', 'boolean', 'real','if', 'return', 'print', 'scan', 'while', 'endwhile' ]
operators = ['<=', '=>', '>', '<', '=', '==', '!=', '+', '-', '/', '*']
separators = ['(', ')', ',', ';', '{', '}', '$']
lexeme = []
tokens = []
count = 0

id_transition_table = {
    1: {'L': 2, 'D': 6, '_': 6, 'Other': 6},
    2: {'L': 3, 'D': 4, '_': 5, 'Other': 6},
    3: {'L': 4, 'D': 4, '_': 5, 'Other': 6},
    4: {'L': 3, 'D': 4, '_': 5, 'Other': 6},
    5: {'L': 3, 'D': 4, '_': 5, 'Other': 6},
    6: {'L': 6, 'D': 6, '_': 6, 'Other': 6},
}

real_transition_table = {
    1: {'D': 2, '.': 5, 'Other': 5},
    2: {'D': 2, '.': 3, 'Other': 5},
    3: {'D': 4, '.': 5, 'Other': 5},
    4: {'D': 4, '.': 5, 'Other': 5},
    5: {'D': 5, '.': 5, 'Other': 5},
}

int_transition_table = {
    1: {'D': 2, 'Other': 3},
    2: {'D': 2, 'Other': 3}, 
    3: {'D': 3, 'Other': 3},
}

def char_to_col(ch):
    if ch.isalpha():
        return 'L'
    elif ch.isdigit():
        return 'D'
    elif ch == '_':
        return '_'
    elif ch == '.':
        return '.'
    else:
        return 'Other'
    
    # DFSM ID
def DFSM_ID(string_input, transition_table):
    state = 1
    accepting_states = {2, 3, 4, 5}

    for char in string_input:
        col = char_to_col(char)
        state = transition_table[state].get(col, 6)

    return 1 if state in accepting_states else 0


# DFSM REAL
def DFSM_REAL(string_input, transition_table):
    state = 1
    accepting_states = {4}

    for char in string_input:
        col = char_to_col(char)
        state = transition_table[state].get(col, 5)

    return 1 if state in accepting_states else 0


# DFSM INT
def DFSM_INT(string_input, transition_table):
    state = 1
    accepting_states = {2}

    for char in string_input:
        col = char_to_col(char)
        state = transition_table[state].get(col, 3)

    return 1 if state in accepting_states else 0

# remove_comments(): removes comments from string input
# Arguments: string input taken from test case file
# Returns: modified input string with comments removed
def remove_comments(input_string):
    start_comment = input_string.find("[*")
    while start_comment != -1:
        end_comment = input_string.find("*]", start_comment + 2)
        if end_comment == -1:
            # If there's no matching end comment, remove everything after the start comment
            input_string = input_string[:start_comment]
            break
        input_string = input_string[:start_comment] + input_string[end_comment + 2:]
        start_comment = input_string.find("[*", start_comment)
    return input_string


def lexer(input):
    global tokens
    global id_transition_table
    global int_transition_table
    global real_transition_table

    if input in operators:
        tokens.append(('Operator', input))
    elif input in keywords:
        tokens.append(('Keyword', input))
    elif input in separators: 
        tokens.append(('Separator', input))
    elif input[0] in separators or input[0] in operators or input[0].isdigit() or input[0].isalpha() or input[0] == '!' or input[0] == '.' or input[0] == '_':
        input += " "
        current_str = ""
        input_iter = iter(input)
        for char in input_iter:
            length = len(current_str)
            if (((char in separators) or (char in operators) or (char.isspace()) or (char == '!')) and (length == 0)):
                if char in separators:
                    tokens.append(('Separator', char))
                elif char == '<' or char == '=' or char == '!':
                    current_str = char
                elif char in operators:
                    tokens.append(('Operator', char))
                continue
            if (((char in separators) or (char in operators) or (char.isspace()) or (char == '!')) and (length > 0)):
                if current_str[0] in operators or current_str[0] == '!':
                    if current_str[0] == '<':
                        if char == '=':
                            current_str += char
                            tokens.append(('Operator', current_str))
                            current_str = ""
                        elif char in operators:
                            current_str += char
                            tokens.append(('Unknown', current_str))
                            current_str = ""
                    elif current_str[0] == '=':
                        if char == '>' or char == '=':
                            current_str += char
                            tokens.append(('Operator', current_str))
                            current_str = ""
                        elif char in operators:
                            current_str += char
                            tokens.append(('Unknown', current_str))
                            current_str = ""
                    elif current_str[0] == '!':
                        if char == '=':
                            current_str += char
                            tokens.append(('Operator', current_str))
                            current_str = ""
                        elif char in operators:
                            current_str += char
                            tokens.append(('Unknown', current_str))
                            current_str = ""
                    else:
                        current_str = char
                    continue
                
                elif current_str[0].isdigit() or current_str[0] == '.':
                    if DFSM_REAL(current_str, real_transition_table):
                        tokens.append(('Real', current_str))
                    elif DFSM_INT(current_str, int_transition_table):
                        tokens.append(('Integer', current_str))
                    else:
                        tokens.append(('Unknown', current_str))
                    current_str = ""

                elif current_str[0].isalpha() or current_str == '_':
                    if current_str in keywords:
                        tokens.append(('Keyword', current_str))
                    elif DFSM_ID(current_str, id_transition_table):
                        tokens.append(('Identifier', current_str))
                    else:
                        tokens.append(('Unknown', current_str))

                    current_str = ""
                
                if char in separators:
                    tokens.append(('Separator', char))
                elif char == '<' or char == '=' or char == '!':
                    current_str = char
                elif char in operators:
                    tokens.append(('Operator', char))
                
            
            elif char.isdigit() or char.isalpha() or char == '.' or char == '_':
                current_str += char 
            else:
                tokens.append(('Unknown', char))

    else:  
        tokens.append(('Unknown', input))
        

def main():
    input_file = "test_case_two.txt"
    output_file = "output_file.txt"
    with open(input_file, 'r') as file:
        input_string = file.read() 
        if not input_string:
            print("File is empty")
            return
        
    input_string_no_comments = remove_comments(input_string)
    input_list = input_string_no_comments.split()

    for input in input_list:
        lexer(input)

    with open(output_file, 'w') as file:
        for token_type, token_value in tokens:
            file.write(f"{token_type} {token_value}\n")
 
    #print(tokens, '\n')


if __name__ == "__main__":
    main()

