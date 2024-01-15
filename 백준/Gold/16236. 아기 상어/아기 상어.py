import sys
from collections import deque

input = sys.stdin.readline

# 상 좌 우 하
dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]


def find_fish(shark_y, shark_x):
    visited = [[False] * n for _ in range(n)]
    distance = [[0] * n for _ in range(n)]
    deq = deque()
    deq.append([shark_y, shark_x])

    can_eat = []
    while deq:
        y, x = deq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < n and 0 <= ny < n:
                # 이동 가능
                if board[ny][nx] <= shark_size and not visited[ny][nx]:
                    visited[ny][nx] = True
                    distance[ny][nx] = distance[y][x] + 1
                    deq.append([ny, nx])

                    # 물고기가 있고 먹을 수 있는 경우
                    if board[ny][nx] < shark_size and board[ny][nx] != 0:
                        can_eat.append([ny, nx, distance[ny][nx]])

    can_eat.sort(key=lambda x: (x[2], x[0], x[1]))  # 거리, y, x 오름차순
    return can_eat


def find_shark():
    for i in range(n):
        for j in range(n):
            if board[i][j] == 9:
                board[i][j] = 0
                return i, j


if __name__ == '__main__':
    n = int(input())
    board = []

    for _ in range(n):
        board.append(list(map(int, input().rstrip().split())))

    shark_y, shark_x = find_shark()
    shark_size = 2
    eat_cnt = 0
    time = 0

    while True:
        fish = find_fish(shark_y, shark_x)
        if len(fish) == 0:
            break

        shark_y, shark_x, t = fish[0]

        eat_cnt += 1
        if shark_size == eat_cnt:
            shark_size += 1
            eat_cnt = 0

        board[shark_y][shark_x] = 0  # 물고기 먹은자리 빈칸
        time += t

    print(time)
