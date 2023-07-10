def solution(numbers):
    answer = -1
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            temp = numbers[i] * numbers[j]
            if answer < temp:
                answer = temp
    return answer