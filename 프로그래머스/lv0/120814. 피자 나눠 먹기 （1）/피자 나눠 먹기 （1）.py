def solution(n):
    num = n // 7
    if n % 7 == 0:
        return num
    else:
        return num + 1