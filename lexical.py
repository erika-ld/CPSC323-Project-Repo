keywords = [
    'endif', 'else', 'function', 'integer', 'true', 'false', 'boolean', 'real',
    'if', 'return', 'print', 'scan', 'while', 'endwhile'
]
operators = ['<=', '>=', '>', '<', '=', '==', '!=', '+', '-', '/', '*']
separators = ['(', ')', ',', ';', '{', '}', '$']
tokens = []

id_transition_table = {
    1: {
        'L': 2,
        'D': 6,
        '_': 6,
        'Other': 6
    },
    2: {
        'L': 3,
        'D': 4,
        '_': 5,
        'Other': 6
    },
    3: {
        'L': 4,
        'D': 4,
        '_': 5,
        'Other': 6
    },
    4: {
        'L': 3,
        'D': 4,
        '_': 5,
        'Other': 6
    },
    5: {
        'L': 3,
        'D': 4,
        '_': 5,
        'Other': 6
    },
    6: {
        'L': 6,
        'D': 6,
        '_': 6,
        'Other': 6
    },
}

real_transition_table = {
    1: {
        'D': 2,
        '.': 5,
        'Other': 5
    },
    2: {
        'D': 2,
        '.': 3,
        'Other': 5
    },
    3: {
        'D': 4,
        '.': 5,
        'Other': 5
    },
    4: {
        'D': 4,
        '.': 5,
        'Other': 5
    },
    5: {
        'D': 5,
        '.': 5,
        'Other': 5
    },
}

int_transition_table = {
    1: {
        'D': 2,
        'Other': 3
    },
    2: {
        'D': 2,
        'Other': 3
    },
    3: {
        'D': 3,
        'Other': 3
    },
}


# return the next token from the index input
def get_next_token(index):
  return tokens[index + 1]


comment_state = False


def lexer(input):
  global comment_state

  if input == '[*':
    comment_state = True
  elif input in keywords:
    print("Keyword found:", input)
    tokens.append(input)
  elif input in operators:
    print("Operator found:", input)
    tokens.append(input)
  elif input[0] in separators and len(input) > 1:
    next_token = input[1:]
    print("Separator found:", input[0])
    tokens.append(input[0])
    lexer(next_token)
  elif input in separators:
    print("Separator found:", input)
    tokens.append(input)
  elif input[0].isalpha() and len(input) > 1:
    if input[-1] in separators:
      print("Identifier found:", input[0:-1])
      print("Separator found:", input[-1])
      tokens.append(input[0:-1])
      tokens.append(input[-1])
    else:
      print("Identifier found:", input)
      tokens.append(input)
  elif input[0].isalpha():
    print("Identifier found:", input)
    tokens.append(input)
  elif input[0].isdigit() and '.' in input:
    check_real_index = input.index('.')
    try:
      if input[check_real_index + 1].isdigit():
        if input[-1] in separators:
          print("Real found: ", input[0:-1])
          print("Separator found:", input[-1])
          tokens.append(input[0:-1])
          tokens.append(input[-1])
        else:
          print("Real found: ", input)
          tokens.append(input)
      else:
        print("Unknown token:", input)
    except IndexError:
      print("Unknown token:", input)
  elif input[0].isdigit():
    if input[-1] in separators:
      print("Integer found: ", input[0:-1])
      print("Separator found:", input[-1])
      tokens.append(input[0:-1])
      tokens.append(input[-1])
    else:
      print("Integer found: ", input)
      tokens.append(input)

  else:
    print("Unknown token:", input)
    tokens.append(input)
    # might not need this line for assigment 2


def main():
  global comment_state
  with open('test_case_one.txt', 'r') as file:
    contents = file.read()
    if not contents:
      print("File is empty")
      return

    token_list = contents.split()
    # print("Token list:", token_list)
    for token in token_list:
      if comment_state is True and token != '*]':
        continue
      elif comment_state is True and token == '*]':
        comment_state = False
      else:
        lexer(token)

  print(tokens)
  # print(get_next_token(1))


if __name__ == "__main__":
  main()
