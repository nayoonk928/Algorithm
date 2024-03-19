from itertools import permutations

def calculate(expression, op_priority):
    temp = []
    num = ""
    for char in expression:
        if char.isdigit():
            num += char
        else:
            temp.append(int(num))
            temp.append(char)
            num = ""
    temp.append(int(num))

    for op in op_priority:
        stack = []
        i = 0
        while i < len(temp):
            if temp[i] == op:
                if op == "+":
                    stack[-1] += temp[i + 1]
                elif op == "-":
                    stack[-1] -= temp[i + 1]
                elif op == "*":
                    stack[-1] *= temp[i + 1]
                i += 1
            else:
                stack.append(temp[i])
            i += 1
        temp = stack

    return abs(temp[0])


def solution(expression):
    answer = 0
    operators = set()
    for char in expression:
        if not char.isdigit():
            operators.add(char)
    operator_permutations = permutations(operators)
    max_result = 0
    for op_priority in operator_permutations:
        max_result = max(max_result, calculate(expression, op_priority))
    answer = max_result
    return answer