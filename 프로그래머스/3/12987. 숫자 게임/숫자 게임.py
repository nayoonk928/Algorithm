def solution(A, B):
    # A 팀과 B 팀의 숫자를 정렬합니다.
    A.sort()
    B.sort()
    
    answer = 0
    a_idx = 0
    b_idx = 0
    
    # A 팀원이 출전하는 숫자와 B 팀원이 출전하는 숫자를 비교하여 승점을 계산합니다.
    while a_idx < len(A) and b_idx < len(B):
        if A[a_idx] < B[b_idx]:
            answer += 1
            a_idx += 1
            b_idx += 1
        else:
            b_idx += 1
    
    return answer
