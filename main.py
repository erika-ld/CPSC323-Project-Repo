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


def DFSM_ID(string_input, transition_table):
    state = 1
    accepting_states = {2, 3, 4, 5}

    for char in string_input:
        col = char_to_col(char)
        state = transition_table[state].get(col, 6)

    return 1 if state in accepting_states else 0

def DFSM_REAL(string_input, transition_table):
    state = 1
    accepting_states = {2, 4}

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
                if DFSM_ID(current_token, transition_table):
                    tokens.append(('Identifier', current_token))
                else:
                    tokens.append(('Invalid', current_token))   
                current_token = ''  
        else: 
            col = char_to_col(char)
            state = transition_table[state].get(col, 6)

            if state == 6:  
                if current_token:
                    if DFSM_ID(current_token, transition_table):
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
        if DFSM_ID(current_token, transition_table):
            tokens.append(('Identifier', current_token))
        else:
            tokens.append(('Invalid', current_token))

    return tokens



def main():
    input_file = "test_case_one.txt"
    output_file = "output.txt"
    with open(input_file, 'r') as file:
        input_string = file.read()

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

    tokens = lexer(input_string, id_transition_table)

    with open(output_file, 'w') as file:
        for token_type, token_value in tokens:
            file.write(f"{token_type}: {token_value}\n")

if __name__ == "__main__":
    main()