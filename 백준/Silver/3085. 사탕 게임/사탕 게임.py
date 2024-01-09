# 백준 3085번 사탕 게임
# 1. 사탕의 색이 다른 인접한 두 칸 고르기
# 1-1. 1번에서 고른 사탕 서로 교환
# 2. 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 or 열) 찾기
import sys

input = sys.stdin.readline

n = int(input())
candies = []


def max_candies(candies):
    max_sum = 1  # 최소 1개의 사탕은 있어야 하므로 1로 초기화

    for i in range(n):
        for j in range(n):
            current = candies[i][j]

            # 오른쪽과 교환 (i + 1 < n인 경우)
            if i + 1 < n:
                right = candies[i + 1][j]
                candies[i][j], candies[i + 1][j] = right, current
                max_sum = max(max_sum, find_max_length(candies))
                candies[i][j], candies[i + 1][j] = current, right  # 원래대로 되돌리기

            # 아래쪽과 교환 (j + 1 < n인 경우)
            if j + 1 < n:
                down = candies[i][j + 1]
                candies[i][j], candies[i][j + 1] = down, current
                max_sum = max(max_sum, find_max_length(candies))
                candies[i][j], candies[i][j + 1] = current, down  # 원래대로 되돌리기

    print(max_sum)


def find_max_length(candies):
    max_length = 1

    # 행 기준으로 최대 연속 부분 찾기
    for i in range(n):
        length = 1
        for j in range(1, n):
            if candies[i][j] == candies[i][j - 1]:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
                continue

        max_length = max(max_length, length)

    # 열 기준으로 최대 연속 부분 찾기
    for j in range(n):
        length = 1
        for i in range(1, n):
            if candies[i][j] == candies[i - 1][j]:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
                continue

        max_length = max(max_length, length)

    return max_length


for _ in range(n):
    line = input().strip()
    candies.append(list(line))

max_candies(candies)
