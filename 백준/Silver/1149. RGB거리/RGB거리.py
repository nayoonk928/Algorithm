import sys
input = sys.stdin.readline


def paint():
    dp = [[0] * 3 for _ in range(n)]

    dp[0] = list(map(int, graph[0]))
    for i in range(1, n):
        for j in range(3):
            prev = min(dp[i - 1][(j + 1) % 3], dp[i - 1][(j + 2) % 3])
            dp[i][j] = prev + graph[i][j]

    return min(dp[n - 1])


if __name__ == '__main__':
    n = int(input())
    graph = [[] for _ in range(n)]

    for i in range(n):
        r, g, b = map(int, input().split())
        graph[i] = [r, g, b]

    print(paint())