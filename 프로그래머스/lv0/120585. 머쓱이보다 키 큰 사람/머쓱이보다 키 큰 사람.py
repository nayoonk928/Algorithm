def solution(array, height):
    answer = 0
    array.sort()
    for num in reversed(array):
        if num > height:
            answer += 1
    return answer