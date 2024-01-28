import sys

input = sys.stdin.readline

if __name__ == "__main__":
    k = int(input())
    nums = []

    for _ in range(k):
        n = int(input())
        if n == 0:
            nums.pop()
            continue

        nums.append(n)

    print(sum(nums))
