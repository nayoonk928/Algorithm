import sys

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(x, y, visited, is_color_weakness):
    stack = [(x, y)]
    color = picture[x][y]
    visited[x][y] = True

    while stack:
        curr_x, curr_y = stack.pop()

        for i in range(4):
            nx, ny = curr_x + dx[i], curr_y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if is_color_weakness:
                    if (color == 'R' or color == 'G') and (picture[nx][ny] == 'R' or picture[nx][ny] == 'G'):
                        stack.append((nx, ny))
                        visited[nx][ny] = True
                    else:
                        if picture[nx][ny] == color:
                            stack.append((nx, ny))
                            visited[nx][ny] = True
                else:
                    if picture[nx][ny] == color:
                        stack.append((nx, ny))
                        visited[nx][ny] = True


def count(is_color_weakness):
    visited = [[False] * n for _ in range(n)]
    region_count = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                dfs(i, j, visited, is_color_weakness)
                region_count += 1

    return region_count


if __name__ == '__main__':
    n = int(input())
    picture = []

    for _ in range(n):
        row = list(input().strip())
        picture.append(row)

    normal_vision = count(False)
    color_weakness = count(True)

    print(normal_vision, color_weakness)