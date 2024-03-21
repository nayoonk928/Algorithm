from collections import deque

def solution(board):
    n, m = len(board), len(board[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 우, 하, 상, 좌
    visited = [[False] * m for _ in range(n)]
    
    # 시작 위치와 목표 위치 찾기
    start, goal = None, None
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)
    
    # BFS 시작
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    while queue:
        x, y, count = queue.popleft()
        if (x, y) == goal:
            return count  # 목표에 도달했다면 이동 횟수 반환
        
        for dx, dy in directions:
            nx, ny, ncount = x, y, count
            # 장애물이나 게임판의 끝에 도달할 때까지 같은 방향으로 이동
            while True:
                nx += dx
                ny += dy
                if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == 'D':
                    nx -= dx
                    ny -= dy
                    break
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, ncount + 1))
                
    return -1  # 목표에 도달할 수 없는 경우