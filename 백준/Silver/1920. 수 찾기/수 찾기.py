n = int(input())
a = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

a.sort()

for target in targets:
    start = 0  # 맨 처음 위치
    end = n - 1  # 맨 마지막 위치
    exist = False  # a에 존재하는지 여부

    while start <= end:
        mid = (start + end) // 2  # 중간값

        if a[mid] == target:
            exist = True
            break
        elif a[mid] > target:
            end = mid - 1
        elif a[mid] < target:
            start = mid + 1

    if exist:
        print(1)
    else:
        print(0)