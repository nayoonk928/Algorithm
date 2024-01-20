import sys
import heapq

input = sys.stdin.readline


def dijkstra(x, y, n):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    lost[x][y] = 0
    pq = []
    heapq.heappush(pq, (0, 0, 0))  # lost, x, y

    while pq:
        l, x, y = heapq.heappop(pq)

        if lost[x][y] != l:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                cost = l + cave[nx][ny]
                if cost < lost[nx][ny]:
                    lost[nx][ny] = cost
                    heapq.heappush(pq, (cost, nx, ny))


if __name__ == '__main__':
    cnt = 1
    while True:
        n = int(input())

        if n == 0:
            break

        lost = [[int(1e9)] * n for _ in range(n)]
        cave = []
        for _ in range(n):
            cave.append(list(map(int, input().split())))

        dijkstra(0, 0, n)

        result = cave[0][0] + lost[n - 1][n - 1]
        print(f"Problem {cnt}: {result}")
        cnt += 1