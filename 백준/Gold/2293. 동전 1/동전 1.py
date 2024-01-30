import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]

    dp = [0 for _ in range(k + 1)]
    dp[0] = 1

    # 각 동전마다 경우의 수를 누적해가면서 계산
    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]

    print(dp[-1])
