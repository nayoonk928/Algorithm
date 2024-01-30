import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    dp = [float('inf')] * (k + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[k] == float('inf'):
        print(-1)
    else:
        print(dp[k])
