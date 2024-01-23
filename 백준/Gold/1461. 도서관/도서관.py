import sys

input = sys.stdin.readline


def move_positive(positive, max_dist):
    steps = 0
    for i in range(0, len(positive), m):
        if positive[i] != max_dist:
            steps += positive[i]

    return steps


def move_negative(negative, max_dist):
    steps = 0
    for i in range(0, len(negative), m):
        if negative[i] != max_dist:
            steps += abs(negative[i])

    return steps


def steps():
    negative = []
    positive = []
    max_dist = 0

    for book in books:
        if book < 0:
            negative.append(book)
        else:
            positive.append(book)

        if abs(book) > abs(max_dist):
            max_dist = book

    negative.sort()
    positive.sort(reverse=True)

    total_steps = move_positive(positive, max_dist) + move_negative(negative, max_dist)
    total_steps *= 2
    total_steps += abs(max_dist)

    return total_steps


if __name__ == '__main__':
    n, m = map(int, input().split())  # 책의 개수, 한 번에 들 수 있는 책의 개수
    books = list(map(int, input().split()))

    print(steps())