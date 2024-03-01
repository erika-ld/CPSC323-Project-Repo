import os
keywords = ['endif', 'else', 'function', 'integer', 'true', 'false',
            'boolean', 'real', 'if', 'return', 'print', 'scan', 'while', 'endwhile']
operators = ['<=', '>=', '>', '<', '=', '==', '!=', '+', '-', '/', '*']
separators = ['(', ')', ',', ';', '{', '}']


def char_to_col(ch):
    if ch.isalpha():
        return 'L'
    elif ch.isdigit():
        return 'D'
    elif ch == '_':
        return '_'
    else:
        return 'Other'


def DFSM(string_input, transition_table):
    state = 1
    accepting_states = {2, 3, 4, 5}

    for char in string_input:
        col = char_to_col(char)
        state = transition_table[state].get(col, 6)

    return 1 if state in accepting_states else 0


def lexer(input_string, transition_table):
    tokens = []
    current_token = ''
    state = 1

    for char in input_string:
        if char.isspace(): 
            if current_token.strip(): 
                if DFSM(current_token, transition_table):
                    tokens.append(('Identifier', current_token))
                else:
                    tokens.append(('Invalid', current_token))   
                current_token = ''  
        else: 
            col = char_to_col(char)
            state = transition_table[state].get(col, 6)

            if state == 6:  
                if current_token:
                    if DFSM(current_token, transition_table):
                        tokens.append(('Identifier', current_token))
                    else:
                        tokens.append(('Invalid', current_token))
                    current_token = ''
                state = 1  
            elif state == 7:  # State for recognizing operators and separators
                current_token = ''  # Reset current token when encountering operator or separator
            else:  
                current_token += char

    if current_token: 
        if DFSM(current_token, transition_table):
            tokens.append(('Identifier', current_token))
        else:
            tokens.append(('Invalid', current_token))

    return tokens


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


def main():
    input_file = "test_case_one.txt"
    output_file = "output.txt"
    temp_file = "temp.txt"

    # Read input file
    with open(input_file, 'r') as file:
        input_string = file.read()

    # Remove comments from input string
    input_string_no_comments = remove_comments(input_string)

    # Write modified input to a temporary file
    with open(temp_file, 'w') as temp:
        temp.write(input_string_no_comments)

    id_transition_table = {
        1: {'L': 2, 'D': 6, '_': 6, 'Other': 6},
        2: {'L': 3, 'D': 4, '_': 5, 'Other': 6},
        3: {'L': 4, 'D': 4, '_': 5, 'Other': 6},
        4: {'L': 3, 'D': 4, '_': 5, 'Other': 6},
        5: {'L': 3, 'D': 4, '_': 5, 'Other': 6},
        6: {'L': 6, 'D': 6, '_': 6, 'Other': 6},
    }

    # Perform lexical analysis on modified input
    tokens = lexer(input_string_no_comments, id_transition_table)

    # Write tokens to output file
    with open(output_file, 'w') as file:
        for token_type, token_value in tokens:
            file.write(f"{token_type}: {token_value}\n")

    # Write keywords, operators, and separators to output file
    with open(output_file, 'a') as file:
        for keyword in keywords:
            if keyword in input_string_no_comments:
                file.write('Keywords: '+ keyword + "\n")

        for operator in operators:
            if operator in input_string_no_comments:
                file.write('Operators: ' + operator + "\n")

        for separator in separators:
            if separator in input_string_no_comments:
                file.write('Separators: '+ separator + "\n")

    # Remove temporary file
    os.remove(temp_file)

if __name__ == "__main__":
    main()
