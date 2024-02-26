def solution(n, s):
    if n > s:
        return [-1]  # n이 s보다 클 경우, 최고의 집합이 존재하지 않음
    
    quotient = s // n  # 몫
    remainder = s % n  # 나머지
    
    answer = [quotient] * n  # 몫으로 초기화
    
    # 남은 나머지를 큰 수부터 1씩 더해가며 배분
    for i in range(1, remainder + 1):
        answer[-i] += 1
    
    return answer