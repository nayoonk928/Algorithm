import sys

input = sys.stdin.readline

if __name__ == "__main__":
    parentheses  = input().strip()

    stack = []
    pieces = 0

    for i in range(len(parentheses)):
        if parentheses[i] == '(':
            stack.append(i)
        else:
            if stack[-1] == i - 1:
                # 레이저인 경우
                stack.pop()
                pieces += len(stack)
            else:
                # 쇠막대기의 끝인 경우
                stack.pop()
                pieces += 1

    print(pieces)