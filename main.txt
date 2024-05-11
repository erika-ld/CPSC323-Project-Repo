import os

# Lists of 3 hardcoded tokens: Keywords, Operators, Separators
keywords = ['endif', 'else', 'function', 'integer', 'true', 'false',
            'boolean', 'real', 'if', 'return', 'print', 'scan', 'while', 'endwhile']
operators = ['<=', '>=', '>', '<', '=', '==', '!=', '+', '-', '/', '*']
separators = ['(', ')', ',', ';', '{', '}', '$']

# char_to_col(): takes char argument ch and outputs the correct category of input
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

# DFSM Functions for Identifier, Integer, and Real
# Arguments: string input and transition table for corresponding token
# Returns: 1 if state is in accepting state, 0 for other

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



# lexer(): evaluates each char in string input and calls corresponding DFSM functions to maintain token list
# Arguments: string input & 3 transition tables for Identifier, Integer, and Reals
# Returns: tokens list containing the processed tokens
def lexer(input_string, id_transition_table, int_transition_table, real_transition_table):
    tokens = []
    current_token = ''
    id_state = 1
    real_state = 1
    int_state = 1

    for char in input_string:
        if char.isspace() or char in operators or char in separators:
            if char in separators:
                        print('Separator:', char)
                        current_token = ''
            elif char in operators:
                        print('Operator:', char)
                        current_token = ''
            elif current_token.strip():
                if current_token[0].isalpha():
                    if current_token in keywords:
                        print('Keyword:', current_token)
                        current_token = ''  # Skip adding keywords to tokens list
                    elif DFSM_ID(current_token, id_transition_table):
                        tokens.append(('Identifier', current_token))
                        print('Identifier:', current_token)
                    else:
                        tokens.append(('Invalid', current_token))
                        print('Invalid:', current_token)
                else:
                    if current_token in keywords:
                        print('Keyword:', current_token)
                        current_token = ''  # Skip adding keywords to tokens list
                    elif DFSM_REAL(current_token, real_transition_table):
                        tokens.append(('Real:', current_token))
                        print('Real:', current_token)
                    else:
                        if DFSM_INT(current_token, int_transition_table):
                            tokens.append(('Int', current_token))
                            print('Int:', current_token)
                        else:
                            tokens.append(('Invalid', current_token))
                            print('Invalid:', current_token)
                current_token = ''
        else:
            col = char_to_col(char)
            if char.isdigit():
                if current_token == '.':
                    real_state = real_transition_table[real_state].get(col, 5)
                    if real_state == 5:
                        tokens.append(('Invalid', current_token))
                        print('Invalid:', current_token)
                        current_token = ''
                        real_state = 1
                    else:
                        current_token += char
                else:
                    int_state = int_transition_table[int_state].get(col, 3)
                    if int_state == 3:
                        tokens.append(('Int', current_token))
                        print('Int:', current_token)
                        current_token = char
                        int_state = 1
                    else:
                        current_token += char
            elif char == '.':
                if current_token.isdigit():
                    current_token += char
                else:
                    tokens.append(('Invalid', current_token))
                    print('Invalid:', current_token)
                    current_token = char
            else:
                id_state = id_transition_table[id_state].get(col, 6)
                if id_state == 6:
                    if current_token:
                        if DFSM_ID(current_token, id_transition_table):
                            tokens.append(('Identifier', current_token))
                            print('Identifier:', current_token)
                        else:
                            tokens.append(('Invalid', current_token))
                            print('Invalid:', current_token)
                        current_token = ''
                    id_state = 1
                else:
                    current_token += char
    if current_token:
        if current_token[0].isalpha():
            if current_token in keywords:
                current_token = ''  # Skip adding keywords to tokens list
            elif DFSM_ID(current_token, id_transition_table):
                tokens.append(('Identifier', current_token))
                print('Identifier:', current_token)
            else:
                tokens.append(('Invalid', current_token))
                print('Invalid:', current_token)
        else:
            if current_token in keywords:
                current_token = ''  # Skip adding keywords to tokens list
            elif DFSM_REAL(current_token, real_transition_table):
                tokens.append(('Real', current_token))
                print('Real:', current_token)
            else:
                if DFSM_INT(current_token, int_transition_table):
                    tokens.append(('Int', current_token))
                    print('Int:', current_token)
                else:
                    tokens.append(('Invalid', current_token))
                    print('Invalid:', current_token)

    # Remove empty entries from tokens
    tokens = [(token_type, token_value) for token_type, token_value in tokens if token_value.strip()]

    return tokens



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

# main(): reads and writes to files, calls lexer() function, and contains transition tables for Identifier, Integer, and Real
def main():
    input_files = ("test_case_one.txt", "test_case_two.txt", "test_case_three.txt")

    temp_file = "temp.txt"

    for input_file in input_files:
        # Get the base name of the input file
        base_name = os.path.basename(input_file)

        # Construct the output file name by appending "_output" to the base name
        output_file = os.path.splitext(base_name)[0] + "_output.txt"

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

if __name__ == "__main__":
    main()
