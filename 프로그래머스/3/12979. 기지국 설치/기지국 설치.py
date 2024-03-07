def solution(n, stations, w):
    answer = 0
    start = 1
    index = 0
    
    # 첫 아파트부터 마지막 아파트까지 반복
    while start <= n:
        # 현재 위치가 기지국의 범위 안에 있는 경우
        if index < len(stations) and start >= stations[index] - w:
            # 기지국의 범위를 넘어서까지 이동
            start = stations[index] + w + 1
            index += 1
        else:
            # 추가 기지국 설치
            answer += 1
            # 다음 아파트로 이동
            start += 2 * w + 1
            
    return answer