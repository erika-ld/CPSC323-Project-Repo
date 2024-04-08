keywords = [
    'endif', 'else', 'function', 'integer', 'true', 'false', 'boolean', 'real',
    'if', 'return', 'print', 'scan', 'while', 'endwhile'
]
operators = ['<=', '>=', '>', '<', '=', '==', '!=', '+', '-', '/', '*']
separators = ['(', ')', ',', ';', '{', '}', '$']
lexeme = []
tokens = []
comment_state = False
output_state = False

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

# Return the next lexeme from the index input
def get_lexeme(index):
    global comment_state, output_state
    output_state = True

    # Change input file if needed
    with open('test_case_one.txt', 'r') as file:
        contents = file.read()
        if not contents:
            print("File is empty")
            return

        token_list = contents.split()
        for token in token_list:
            if comment_state is True and token != '*]':
                continue
            elif comment_state is True and token == '*]':
                comment_state = False
            else:
                lexer(token)

    # Change output file name if needed
    with open('output_case_one.txt', 'w') as file:
        for i in range(len(tokens)):
            file.write(output_token(i) + '\n')

    output_state = False  
    return lexeme[index]

# Return the next token from the index input
def get_token_list(index):
    global comment_state, output_state
    output_state = True

    # Change input file if needed
    with open('test_case_one.txt', 'r') as file:
        contents = file.read()
        if not contents:
            print("File is empty")
            return

        token_list = contents.split()
        for token in token_list:
            if comment_state is True and token != '*]':
                continue
            elif comment_state is True and token == '*]':
                comment_state = False
            else:
                lexer(token)

    # Change output file name if needed
    with open('output_case_one.txt', 'w') as file:
        for i in range(len(tokens)):
            file.write(output_token(i) + '\n')

    output_state = False  
    print("Tokens:", tokens[index], "  Lexeme:", lexeme[index])
    return {tokens[index]: lexeme[index]}

# Return the next token from the index input
def output_token(index):
    return "Tokens: " + tokens[index] + "  Lexeme: " + lexeme[index]

# Lexical analysis function
def lexer(input):
    global comment_state

    # Check comment
    if input == '[*':
        comment_state = True
    # Check keyword
    elif input in keywords:
        if output_state is False:
            print("Keyword found:", input)
        lexeme.append(input)
        tokens.append("Keyword")
    # Check operator
    elif input in operators:
        if output_state is False:
            print("Operator found:", input)
        lexeme.append(input)
        tokens.append("Operator")
    # Check separator
    elif input[0] in separators and len(input) > 1:
        next_token = input[1:]
        if output_state is False:
            print("Separator found:", input[0])
        lexeme.append(input[0])
        tokens.append("Separator")
        lexer(next_token)
    elif input in separators:
        if output_state is False:
            print("Separator found:", input)
        lexeme.append(input)
        tokens.append("Separator")
    # Check identifier
    elif input[0].isalpha() and len(input) > 1:
        if input[-1] in separators:
            if output_state is False:
                print("Identifier found:", input[0:-1])
                print("Separator found:", input[-1])
            lexeme.append(input[0:-1])
            tokens.append("Identifier")
            lexeme.append(input[-1])
            tokens.append("Separator")
        else:
            if output_state is False:
                print("Identifier found:", input)
            lexeme.append(input)
            tokens.append("Identifier")
    elif input[0].isalpha():
        if output_state is False:
            print("Identifier found:", input)
        lexeme.append(input)
        tokens.append("Identifier")
    # Check real
    elif input[0].isdigit() and '.' in input:
        check_real_index = input.index('.')
        try:
            if input[check_real_index + 1].isdigit():
                if input[-1] in separators:
                    if output_state is False:
                        print("Real found:", input[0:-1])
                        print("Separator found:", input[-1])
                    lexeme.append(input[0:-1])
                    tokens.append("Real")
                    lexeme.append(input[-1])
                    tokens.append("Separator")
                else:
                    if output_state is False:
                        print("Real found:", input)
                    lexeme.append(input)
                    tokens.append("Real")
            else:
                if output_state is False:
                    print("Unknown token:", input)
        except IndexError:
            if output_state is False:
                print("Unknown token:", input)
    # Check digit
    elif input[0].isdigit():
        if input[-1] in separators:
            if output_state is False:
                print("Integer found:", input[0:-1])
                print("Separator found:", input[-1])
            lexeme.append(input[0:-1])
            tokens.append("Integer")
            lexeme.append(input[-1])
            tokens.append("Separator")
        else:
            if output_state is False:
                print("Integer found:", input)
            lexeme.append(input)
            tokens.append("Integer")
    # Unknown token
    else:
        if output_state is False:
            print("Unknown token:", input)
        lexeme.append(input)
        tokens.append("Unknown")

# Main function to perform lexical analysis
def main():
    global comment_state
    # Change input file if needed
    with open('test_case_one.txt', 'r') as file:
        contents = file.read()
        if not contents:
            print("File is empty")
            return

        token_list = contents.split()
        for token in token_list:
            if comment_state is True and token != '*]':
                continue
            elif comment_state is True and token == '*]':
                comment_state = False
            else:
                lexer(token)

    # Change output file name if needed
    with open('output_case_one.txt', 'w') as file:
        for i in range(len(tokens)):
            file.write(output_token(i) + '\n')

    print(tokens)

if __name__ == "__main__":
  main()
