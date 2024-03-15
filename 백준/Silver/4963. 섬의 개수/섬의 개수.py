from collections import deque

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

def main():
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

if __name__ == "__main__":
    main()
