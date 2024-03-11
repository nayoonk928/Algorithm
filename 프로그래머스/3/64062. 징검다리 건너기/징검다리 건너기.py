def solution(stones, k):
    # 이진 탐색을 위한 최소값과 최대값 설정
    start, end = 1, max(stones)

    # 이진 탐색 실행
    while start <= end:
        mid = (start + end) // 2  # 중간값을 구하고, 해당 값을 건널 수 있는지 확인
        blank = 0  # 연속된 0이 몇 개 있는지 카운트
        for stone in stones:
            if stone - mid <= 0:  # 해당 친구가 지나간 후의 디딤돌이 0 이하라면
                blank += 1
            else:  # 0보다 크면 연속성이 끊김
                blank = 0
            if blank >= k:  # 연속된 0이 k 이상이면 더 이상 건널 수 없음
                break
        
        if blank < k:  # 연속된 0이 k 미만이면 건널 수 있음, 더 많은 친구를 시도
            start = mid + 1
        else:  # 건널 수 없으면, 더 적은 친구를 시도
            end = mid - 1
    
    return start