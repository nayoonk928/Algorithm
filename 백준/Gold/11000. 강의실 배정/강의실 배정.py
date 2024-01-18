import sys
import heapq
input = sys.stdin.readline


def min_rooms():
    lectures.sort(key=lambda x: x[0])
    classrooms = [lectures[0][1]] 

    for i in range(1, len(lectures)):
        start, end = lectures[i]

        if classrooms[0] <= start:
            heapq.heappop(classrooms)
        heapq.heappush(classrooms, end)

    return len(classrooms)


if __name__ == '__main__':
    n = int(input())
    lectures = []
    for i in range(n):
        s, t = map(int, input().split())
        lectures.append((s, t))

    print(min_rooms())