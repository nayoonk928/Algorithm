from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def bfs(x, y, h, w, field):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, -1, -1, 1]
    queue = deque([(x, y)])
    field[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
                field[nx][ny] = 0
                queue.append((nx, ny))

def dfs(x, y, w, h, field):
    # 방향 벡터: 상, 하, 좌, 우, 대각선 4방향
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    field[x][y] = 0  # 방문한 지점은 0으로 변경
    
    for direction in range(8):
        nx, ny = x + dx[direction], y + dy[direction]
        # 지도 범위 내에 있고, 다음 지점이 땅(1)인 경우 탐색 계속
        if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
            dfs(nx, ny, w, h, field)

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    field = [list(map(int, input().split())) for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1:
                bfs(i, j, h, w, field)
                count += 1
    print(count)
