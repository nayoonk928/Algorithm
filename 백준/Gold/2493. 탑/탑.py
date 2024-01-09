import sys

input = sys.stdin.readline

n = int(input())
towers = list(map(int, input().split()))

answer = []
stack = []

for i, value in enumerate(towers):
    while stack and towers[stack[-1]] < value:
        stack.pop()

    if stack:
        answer.append(stack[-1] + 1)  # index + 1
    else:
        answer.append(0)

    stack.append(i)

print(" ".join(map(str, answer)))