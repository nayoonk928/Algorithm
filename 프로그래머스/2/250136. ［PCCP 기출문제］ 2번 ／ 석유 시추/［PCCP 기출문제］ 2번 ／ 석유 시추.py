import sys
sys.setrecursionlimit(1000000)

def solution(land):
    n = len(land)
    m = len(land[0])
    oils = []  # 각 석유 덩어리의 크기를 저장할 리스트

    visited = [[0 for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def dfs(x, y, l):
        count = 0  # 석유 덩어리의 크기를 저장할 변수
        if x < 0 or x >= m or y < 0 or y >= n:
            return count
        if land[y][x] == 1 and visited[y][x] == 0:
            visited[y][x] = l
            count += 1
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                count += dfs(nx, ny, l)
        return count

    # 각 위치에서 석유 덩어리의 크기를 구하고 oils 리스트에 저장
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == 0:
                l = len(oils) + 1
                oil_size = dfs(j, i, l)
                oils.append(oil_size)

    # 각 열마다 석유 덩어리의 총량을 계산하여 최대값을 반환
    max_oil = 0
    for i in range(m):
        total = set()
        for j in range(n):
            total.add(visited[j][i])
        total = list(total)
        for k in range(len(total)):
            if total[k] > 0:
                total[k] = oils[total[k] - 1]
        max_oil = max(max_oil, sum(total))

    return max_oil