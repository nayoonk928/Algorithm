import sys

input = sys.stdin.readline


def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]
    return merge(mergesort(left), mergesort(right))


if __name__ == '__main__':
    n = int(input())

    nums = []
    for _ in range(n):
        nums.append(int(input()))

    nums = mergesort(nums)

    for i in range(n):
        print(nums[i])