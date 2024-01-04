t = int(input())

for _ in range(t):
    str = input().strip()
    stack = []

    for char in str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                stack.append(')')
                break
            else:
                stack.pop()

    if not stack:
        print("YES")
    else:
        print("NO")