import heapq
import sys
input = sys.stdin.readline

MOD = 10007


def fill_rectangle(n):
    dp = [0] * 1001

    # 초기값 설정
    dp[1] = 1
    dp[2] = 3

    # DP 테이블 채우기
    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % MOD

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    result = fill_rectangle(n)
    print(result)

