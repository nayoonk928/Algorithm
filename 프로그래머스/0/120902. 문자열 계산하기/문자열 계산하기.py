def solution(my_string):
    tokens = my_string.split()

    result = int(tokens[0])

    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        operand = int(tokens[i + 1])

        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand

    return result