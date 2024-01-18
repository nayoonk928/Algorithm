import sys
import heapq
input = sys.stdin.readline


def get_length():
    sensors.sort()

    if n == 1:
        return 0

    heap = []
    for i in range(n - 1):
        heapq.heappush(heap, sensors[i] - sensors[i + 1])

    for _ in range(k - 1):
        heapq.heappop(heap)

    return -sum(heap)


if __name__ == '__main__':
    n = int(input())
    k = int(input()) 
    sensors = list(map(int, input().split()))

    print(get_length())
