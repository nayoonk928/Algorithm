def solution(n):
    answer = [[0] * n for _ in range(n)]  # n x n 배열 초기화
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 우, 하, 좌, 상
    num = 1  # 배열에 채워질 숫자
    
    x, y = 0, 0  # 초기 위치 설정
    d = 0  # 초기 방향 설정
    
    for i in range(1, n * n + 1):  # 총 숫자의 개수만큼 반복
        answer[x][y] = i
        
        # 다음 위치 계산
        nx, ny = x + direction[d][0], y + direction[d][1]
        
        # 다음 위치가 범위를 벗어나거나 이미 숫자가 채워져 있는 경우 방향을 바꿈
        if not (0 <= nx < n and 0 <= ny < n) or answer[nx][ny] != 0:
            d = (d + 1) % 4
            nx, ny = x + direction[d][0], y + direction[d][1]
        
        x, y = nx, ny  # 다음 위치로 이동
        
    return answer