def solution(arr):
    answer = []
    for i in range(len(arr)):
        temp = arr[i]
        if temp >= 50 and temp % 2 == 0:
            answer.append(temp // 2)
        elif temp < 50 and temp % 2 != 0:
            answer.append(temp * 2)
        else:
            answer.append(temp)
    return answer