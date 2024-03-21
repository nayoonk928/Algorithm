from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 상하좌우 이동
    start, lever, exit = None, None, None

    # 시작점(S), 레버(L), 출구(E) 위치 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)

    # BFS 구현을 위한 함수
    def bfs(start, end):
        visited = [[False] * m for _ in range(n)]
        queue = deque([(start[0], start[1], 0)])  # (x좌표, y좌표, 이동 거리)
        visited[start[0]][start[1]] = True

        while queue:
            x, y, dist = queue.popleft()

            if (x, y) == end:
                return dist  # 목표에 도달했을 때의 이동 거리 반환

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

        return -1  # 목표에 도달할 수 없는 경우

    # S에서 L까지, 그리고 L에서 E까지의 최단 거리 계산
    to_lever = bfs(start, lever)
    if to_lever == -1:  # 레버에 도달할 수 없으면 탈출 불가
        return -1
    to_exit = bfs(lever, exit)
    if to_exit == -1:  # 출구에 도달할 수 없으면 탈출 불가
        return -1

    return to_lever + to_exit