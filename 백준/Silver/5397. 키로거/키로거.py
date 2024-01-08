import sys
input = sys.stdin.readline

case = int(input())

for _ in range(case):
    input_pwd = input().rstrip()
    left = []
    right = []

    for char in input_pwd:
        if char == ">":
            if right:
                left.append(right.pop())
        elif char == "<":
            if left:
                right.append(left.pop())
        elif char == "-":
            if left:
                left.pop()
        else:
            left.append(char)

    print("".join(left) + "".join(right[::-1]))
