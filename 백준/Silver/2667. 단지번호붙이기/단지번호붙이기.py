import sys
input = sys.stdin.readline

n = int(input())
my_map = []
for _ in range(n):
    row = list(map(int, input().strip()))
    my_map.append(row)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

rows, cols = len(my_map), len(my_map[0])
house = []


def dfs(x, y):
    my_map[x][y] = 0
    count = 1
    stack = [(x, y)]

    while stack:
        x, y = stack.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < rows and 0 <= ny < cols and my_map[nx][ny] == 1:
                stack.append((nx, ny))
                my_map[nx][ny] = 0
                count += 1

    return count


for row in range(rows):
    for col in range(cols):
        if my_map[row][col] == 1:
            house.append(dfs(row, col))

print(len(house))  # 총 단지 수
for count in sorted(house):  # 단지내 집의 수
    print(count)
