import sys

input = sys.stdin.readline


def check_attach(y, x, rows, cols):
    for i in range(rows):
        for j in range(cols):
            ny = i + y
            nx = j + x
            if sticker[i][j] == 1 and laptop[ny][nx] == 1:
                return False

    return True


def attaching(y, x, rows, cols):
    for i in range(rows):
        for j in range(cols):
            ny = i + y
            nx = j + x
            if sticker[i][j] == 1:
                laptop[ny][nx] = 1


def attach(sticker):
    rows, cols = len(sticker), len(sticker[0])

    for i in range(n - rows + 1):
        for j in range(m - cols + 1):
            if check_attach(i, j, rows, cols):
                attaching(i, j, rows, cols)
                return True

    return False


def rotate(sticker):
    rows, cols = len(sticker), len(sticker[0])

    rotated = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - 1 - i] = sticker[i][j]

    return rotated


if __name__ == '__main__':
    n, m, k = map(int, input().split())
    laptop = [[0] * m for _ in range(n)]
    stickers = []

    result = 0
    for _ in range(k):
        r, c = map(int, input().split())
        sticker = [list(map(int, input().split())) for _ in range(r)]
        stickers.append(sticker)

    for sticker in stickers:
        for i in range(4):
            if attach(sticker):
                break
            sticker = rotate(sticker)

    print(sum(map(sum, laptop)))