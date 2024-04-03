def solution(n, times):
    left, right = 1, max(times) * n  # 최소 시간과 최대 시간 설정
    answer = right  # 최대 시간으로 초기화
    
    while left <= right:
        mid = (left + right) // 2  # 중간 값 계산
        people = sum(mid // time for time in times)  # mid 시간 동안 심사할 수 있는 사람 수
        
        if people >= n:  # 모든 사람을 심사할 수 있는 경우
            answer = min(answer, mid)  # 최소 시간 갱신
            right = mid - 1  # 최대 시간을 줄여 더 작은 시간 탐색
        else:  # 모든 사람을 심사할 수 없는 경우
            left = mid + 1  # 최소 시간을 늘려 더 많은 사람을 심사할 수 있도록 함
            
    return answer