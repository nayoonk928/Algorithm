import sys
from collections import deque

input = sys.stdin.readline

# 상 좌 우 하
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]


def bfs(start, target):
    n = len(board)
    visited = [[False] * n for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = True

    while queue:
        x, y, dist = queue.popleft()

        if (x, y) == target:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] <= shark_size:
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = True

    return -1  # 목표에 도달할 수 없는 경우


def find_fish(shark_x, shark_y):
    n = len(board)
    min_dist = float('inf')
    target_fish = None

    for i in range(n):
        for j in range(n):
            if 1 <= board[i][j] < shark_size and board[i][j] != 9:  # 먹을 수 있는 물고기인 경우
                dist = bfs((shark_x, shark_y, 0), (i, j))
                if dist != -1 and dist < min_dist:
                    min_dist = dist
                    target_fish = (i, j)

    return target_fish, min_dist


def find_shark():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                return (i, j)


if __name__ == '__main__':
    n = int(input())
    board = []

    for _ in range(n):
        board.append(list(map(int, input().rstrip().split())))

    shark_x, shark_y = find_shark()
    shark_size = 2
    eat_cnt = 0
    time = 0

    while True:
        fish, dist = find_fish(shark_x, shark_y)
        if not fish:
            break

        x, y = fish
        board[shark_x][shark_y] = 0  # 아기 상어 위치 초기화
        shark_x, shark_y = x, y  # 아기 상어 위치 업데이트
        board[x][y] = 9  # 아기 상어 이동

        eat_cnt += 1
        if eat_cnt == shark_size:  # 아기 상어 크기만큼 물고기를 먹으면 크기 증가
            shark_size += 1
            eat_cnt = 0

        time += dist

    print(time)