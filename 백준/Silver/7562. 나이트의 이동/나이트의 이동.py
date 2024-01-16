import sys
from collections import deque

input = sys.stdin.readline

moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),
         (-2, -1), (-1, -2), (1, -2), (2, -1)]


def knight_moves(len, start, end):
    queue = deque([(start, 0)])
    visited = [[False] * len for _ in range(len)]
    visited[start[0]][start[1]] = True

    while queue:
        curr, count = queue.popleft()

        if curr == end:
            return count

        for move in moves:
            new_col = curr[0] + move[0]
            new_row = curr[1] + move[1]

            if 0 <= new_col < len and 0 <= new_row < len and not visited[new_col][new_row]:
                queue.append(((new_col, new_row), count + 1))
                visited[new_col][new_row] = True

    return -1


if __name__ == '__main__':
    testcase = int(input())

    for _ in range(testcase):
        len = int(input())
        start = tuple(map(int, input().split()))
        end = tuple(map(int, input().split()))

        result = knight_moves(len, start, end)
        print(result)
