def solution(n, k):
    free = n // 10
    answer = n * 12000 + (k - free) * 2000
    return answer