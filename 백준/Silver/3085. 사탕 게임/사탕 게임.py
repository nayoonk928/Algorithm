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
                max_sum = max(max_sum, find_max_length(candies, i, i + 1, j, j))
                candies[i][j], candies[i + 1][j] = current, right  # 원래대로 되돌리기

            # 아래쪽과 교환 (j + 1 < n인 경우)
            if j + 1 < n:
                down = candies[i][j + 1]
                candies[i][j], candies[i][j + 1] = down, current
                max_sum = max(max_sum, find_max_length(candies, i, i, j, j + 1))
                candies[i][j], candies[i][j + 1] = current, down  # 원래대로 되돌리기

    print(max_sum)


def find_max_length(candies, row_start, row_end, col_start, col_end):
    max_length = 1

    # 행 기준으로 최대 연속 부분 찾기
    for i in range(row_start, row_end + 1):
        length = 1
        for j in range(1, n):
            if candies[i][j] == candies[i][j - 1]:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1

        max_length = max(max_length, length)

    # 열 기준으로 최대 연속 부분 찾기
    for j in range(col_start, col_end + 1):
        length = 1
        for i in range(1, n):
            if candies[i][j] == candies[i - 1][j]:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1

        max_length = max(max_length, length)

    return max_length


for _ in range(n):
    line = input().strip()
    candies.append(list(line))

max_candies(candies)