import sys
import collections
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    nums = collections.deque(range(1, n + 1))

    while len(nums) > 1:
        nums.popleft()
        nums.append(nums.popleft())

    print(nums[0])
