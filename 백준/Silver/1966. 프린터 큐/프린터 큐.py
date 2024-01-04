import sys
from collections import deque

def print_queue(n, m, priority):
    deq = deque()
    max_value = -1
    count = 0

    for i in range(n):
        value = priority[i]
        deq.append((i, value))
        if value > max_value:
            max_value = value

    while len(deq) > 0:
        popped_index, popped_value = deq.popleft()

        if popped_value < max_value:
            deq.append((popped_index, popped_value))
        else:
            count += 1
            if popped_index == m:
                return count
            max_value = max(val for idx, val in deq)

    return count

case = int(sys.stdin.readline())

for _ in range(case):
    n, m = map(int, sys.stdin.readline().split())
    
    priority = list(map(int, sys.stdin.readline().split()))
    print(print_queue(n, m, priority))
