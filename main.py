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
# END DFSM ID


# DFSM REAL
def DFSM_REAL(string_input, transition_table):
    state = 1
    accepting_states = {4}

    for char in string_input:
        col = char_to_col(char)
        state = transition_table[state].get(col, 5)

    return 1 if state in accepting_states else 0
# END DFSM REAL

# DFSM INT
def DFSM_INT(string_input, transition_table):
    state = 1
    accepting_states = {2}

    for char in string_input:
        col = char_to_col(char)
        state = transition_table[state].get(col, 3)

    return 1 if state in accepting_states else 0
# END DFSM INT


# LEXER
def lexer(input_string, id_transition_table, int_transition_table, real_transition_table):
    tokens = []
    current_token = ''
    id_state = 1
    real_state = 1
    int_state = 1

    # for every character inputted
    for char in input_string:
        # if it is a space or an operator/separators
        if char.isspace() or char in operators or char in separators:
            # and the current_token is existent -> return true
            if current_token.strip():
                if current_token[0].isalpha():
                    if current_token in keywords:
                        current_token = ''  # Skip adding keywords to tokens list
                    elif DFSM_ID(current_token, id_transition_table):
                        # add the current_token to the tokens list as an identifier
                        tokens.append(('Identifier', current_token))
                    else:
                        # add the invalid token to the tokens list
                        tokens.append(('Invalid', current_token))
                else:
                    if current_token in keywords:
                        current_token = ''  # Skip adding keywords to tokens list
                    elif DFSM_REAL(current_token, real_transition_table):
                        tokens.append(('Real', current_token))
                    else:
                        if DFSM_INT(current_token, int_transition_table):
                            tokens.append(('Int', current_token))
                        else:
                            tokens.append(('Invalid', current_token))
                # reset the current token
                current_token = ''
        # if it is not a space, and is instead a character
        else:
            # find out which column the char belongs to
            col = char_to_col(char)
            if char.isdigit():
                if current_token == '.':
                    real_state = real_transition_table[real_state].get(col, 5)
                    if real_state == 5:
                        tokens.append(('Invalid', current_token))
                        current_token = ''
                        real_state = 1
                    else:
                        current_token += char
                else:
                    int_state = int_transition_table[int_state].get(col, 3)
                    if int_state == 3:
                        tokens.append(('Int', current_token))
                        current_token = char
                        int_state = 1
                    else:
                        current_token += char
            elif char == '.':
                if current_token.isdigit():
                    current_token += char
                else:
                    tokens.append(('Invalid', current_token))
                    current_token = char
            else:
                id_state = id_transition_table[id_state].get(col, 6)
                if id_state == 6:
                    if current_token:
                        if DFSM_ID(current_token, id_transition_table):
                            tokens.append(('Identifier', current_token))
                        else:
                            tokens.append(('Invalid', current_token))
                        current_token = ''
                    id_state = 1
                else:
                    current_token += char
    # after the for loop
    if current_token:
        if current_token[0].isalpha():
            if current_token in keywords:
                current_token = ''  # Skip adding keywords to tokens list
            elif DFSM_ID(current_token, id_transition_table):
                tokens.append(('Identifier', current_token))
            else:
                tokens.append(('Invalid', current_token))
        else:
            if current_token in keywords:
                current_token = ''  # Skip adding keywords to tokens list
            elif DFSM_REAL(current_token, real_transition_table):
                tokens.append(('Real', current_token))
            else:
                if DFSM_INT(current_token, int_transition_table):
                    tokens.append(('Int', current_token))
                else:
                    tokens.append(('Invalid', current_token))

    # Remove empty entries from tokens
    tokens = [(token_type, token_value) for token_type, token_value in tokens if token_value.strip()]

    return tokens
# END LEXER









# REMOVE COMMENTS
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
#END REMOVE COMMENTS

# MAIN
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

    # Perform lexical analysis on modified input
    tokens = lexer(input_string_no_comments, id_transition_table, int_transition_table, real_transition_table)

    # Write tokens to output file
    with open(output_file, 'w') as file:
        for token_type, token_value in tokens:
            file.write(f"{token_type}: {token_value}\n")
    
    # Write keywords, operators, and separators to output file
    with open(output_file, 'a') as file:
        # Loop through the input string and check for keywords, operators, and separators
        i = 0
        while i < len(input_string_no_comments):
            if input_string_no_comments[i:i+2] in operators:
                file.write('Operators: ' + input_string_no_comments[i:i+2] + "\n")
                i += 2
            elif input_string_no_comments[i] in operators:
                file.write('Operators: ' + input_string_no_comments[i] + "\n")
                i += 1
            elif input_string_no_comments[i] in separators:
                file.write('Separators: ' + input_string_no_comments[i] + "\n")
                i += 1
            else:
                i += 1

        # Check for keywords
        for keyword in keywords:
            if keyword in input_string_no_comments:
                file.write('Keywords: ' + keyword + "\n")

    # Remove temporary file
    os.remove(temp_file)

# END MAIN



if __name__ == "__main__":
    main()
