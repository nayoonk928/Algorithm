import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 0, max(trees)
result = 0

while start <= end:
    mid = (start + end) // 2
    total_length = 0

    for tree in trees:
        if tree > mid:
            total_length += tree - mid

    if total_length >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)