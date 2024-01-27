from collections import deque

def bfs(maze, n, m):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(0, 0, 1)])  # 시작점을 큐에 넣음
    visited = [[False] * m for _ in range(n)]  # 방문 여부를 저장하는 배열

    while queue:
        x, y, count = queue.popleft()

        if x == n - 1 and y == m - 1:  # 도착점에 도달한 경우
            return count

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny, count + 1))
                visited[nx][ny] = True

# 입력 받기
n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]

# 최단 경로 출력
result = bfs(maze, n, m)
print(result)
