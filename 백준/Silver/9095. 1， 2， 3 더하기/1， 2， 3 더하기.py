import sys
from collections import deque

input = sys.stdin.readline


def count_combinations(target):
    ways = 0

    queue = deque([0])

    while queue:
        current_sum = queue.popleft()

        # 현재 합이 목표값에 도달한 경우
        if current_sum == target:
            ways += 1
        # 현재 합이 목표값보다 작은 경우, 가능한 다음 값을 큐에 추가
        elif current_sum < target:
            queue.append(current_sum + 1)
            queue.append(current_sum + 2)
            queue.append(current_sum + 3)

    return ways


if __name__ == "__main__":
    test_case = int(input())

    for _ in range(test_case):
        target = int(input())
        print(count_combinations(target))