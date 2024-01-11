import sys
from collections import deque

input = sys.stdin.readline


# dp
def count_commbinations_dp(target):
    dp = [1, 1, 2, 4]

    for i in range(4, target + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

    return dp[target]


if __name__ == "__main__":
    test_case = int(input())

    for _ in range(test_case):
        target = int(input())
        print(count_commbinations_dp(target))