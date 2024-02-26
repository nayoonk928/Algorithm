def solution(m, n, puddles):
    MOD = 1000000007
    
    # 격자 초기화
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 집은 시작점으로 1로 초기화
    grid[1][1] = 1
    
    # 물에 잠긴 지역은 도달할 수 없으므로 0으로 초기화
    for puddle in puddles:
        grid[puddle[1]][puddle[0]] = -1
    
    # 다이나믹 프로그래밍을 통해 각 칸에 도달할 수 있는 최단 경로의 수 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:  # 시작점은 이미 초기화되어 있음
                continue
            if grid[i][j] == -1:  # 물에 잠긴 지역은 건너뜀
                continue
            if grid[i-1][j] != -1:  # 위쪽 칸으로부터 오는 경우의 수
                grid[i][j] += grid[i-1][j]
            if grid[i][j-1] != -1:  # 왼쪽 칸으로부터 오는 경우의 수
                grid[i][j] += grid[i][j-1]
            grid[i][j] %= MOD
    
    return grid[n][m]  # 학교까지 갈 수 있는 최단 경로의 수