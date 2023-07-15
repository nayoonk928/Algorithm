def solution(age):
    answer = ''
    digits = [int(digit) for digit in str(age)]
    for i in range(len(digits)):
        answer += chr(97 + digits[i])
    return answer