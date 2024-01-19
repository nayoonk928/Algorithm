import sys
input = sys.stdin.readline


def count_cables(cables, target_length):
    count = 0
    for cable in cables:
        count += cable // target_length
    return count


def binary_search(cables, target_count):
    start, end = 1, max(cables)

    while start <= end:
        mid = (start + end) // 2
        current_count = count_cables(cables, mid)

        if current_count >= target_count:
            start = mid + 1
        else:
            end = mid - 1

    return end


if __name__ == "__main__":
    k, n = map(int, input().split())
    lan_cables = [int(input()) for _ in range(k)]

    result = binary_search(lan_cables, n)
    print(result)