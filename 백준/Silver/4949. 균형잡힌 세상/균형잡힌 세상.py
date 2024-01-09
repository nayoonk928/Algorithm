import sys

input = sys.stdin.readline


def is_balanced_string(sentence):
    pair = {
        ')': '(',
        ']': '['
    }
    opener = "(["
    stack = []

    for s in sentence:
        if s in opener:
            stack.append(s)
        elif s in pair:
            if stack and pair[s] == stack[-1]:
                stack.pop()
            else:
                stack.append(s)
                break

    if not stack:
        print("yes")
    else:
        print("no")


while True:
    sentence = input().rstrip()
    if sentence == ".":
        break

    is_balanced_string(sentence)