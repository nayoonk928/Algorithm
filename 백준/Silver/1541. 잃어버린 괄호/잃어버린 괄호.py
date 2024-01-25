expression = input().strip()

result = 0
num = ""
addition = True

for char in expression:
    if char.isdigit():
        num += char
    else:
        num = int(num)
        if addition:
            result += num
        else:
            result -= num

        if char == '-':
            addition = False

        num = ""

# 마지막 숫자 처리
num = int(num)
if addition:
    result += num
else:
    result -= num

print(result)
