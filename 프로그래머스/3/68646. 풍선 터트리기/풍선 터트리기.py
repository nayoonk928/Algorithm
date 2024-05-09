def solution(a):
    answer = 0
    left_min = float('inf')
    right_min = float('inf')

    # 왼쪽에서부터 최소값 업데이트
    for i in range(len(a)):
        if a[i] < left_min:
            left_min = a[i]
            answer += 1

    # 오른쪽에서부터 최소값 업데이트
    for i in range(len(a) - 1, -1, -1):
        if a[i] < right_min:
            right_min = a[i]
            answer += 1

    # 중복으로 더해진 중심 풍선 1개 빼기
    return answer - 1