import sys

input = sys.stdin.readline

# 상 우 하 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def spread():
    new_room = [row[:] for row in room]  # 확산은 동시에 일어나기 때문에 새 리스트 생성

    for y in range(r):
        for x in range(c):
            if room[y][x] <= 0:
                continue

            spread = room[y][x] // 5
            count = 0
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= ny < r and 0 <= nx < c and room[ny][nx] != -1:
                    new_room[ny][nx] += spread
                    count += 1

            new_room[y][x] -= spread * count

    return new_room


def clean():
    # 위 공기청정기 회전
    y, x = top, 1
    before = 0
    index = 1  # 오른쪽 부터 시작
    while True:
        ny = y + dy[index]
        nx = x + dx[index]
        if nx == c or ny == r or nx == -1 or ny == -1:
            index = (index - 1) % 4
            continue
        if x == 0 and y == top:  # 공기청정기로 돌아옴
            break

        room[y][x], before = before, room[y][x]
        y, x = ny, nx

    # 아래쪽 공기청정기 회전
    y, x = bottom, 1
    before = 0
    index = 1  # 오른쪽 부터 시작
    while True:
        ny = y + dy[index]
        nx = x + dx[index]
        if nx == c or ny == r or nx == -1 or ny == -1:
            index = (index + 1) % 4
            continue
        if x == 0 and y == bottom:  # 공기청정기로 돌아옴
            break

        room[y][x], before = before, room[y][x]
        y, x = ny, nx


if __name__ == '__main__':
    r, c, t = map(int, input().rstrip().split())
    room = []
    for _ in range(r):
        room.append(list(map(int, input().rstrip().split())))

    top, bottom = 0, 0
    # 공기청정기 위치 저장
    for i in range(r):
        if room[i][0] == -1:
            top = i
            bottom = i + 1
            break

    for _ in range(t):
        room = spread()
        clean()

    answer = 2
    for i in range(r):
        answer += sum(room[i])

    print(answer)