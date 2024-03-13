def solution(n):
    answer = ''
    while n > 0:
        n, remainder = divmod(n-1, 3) # 1을 빌려오는 과정
        answer = '124'[remainder] + answer # 나머지에 따라 1, 2, 4 중 하나를 선택
    return answer