import sys
from heapq import heappush, heappop

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(heappop(heap))
    else:
        heappush(heap, x)