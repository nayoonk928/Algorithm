import sys
input = sys.stdin.readline

n = int(input())

enter_order = dict()  # 들어간 순서 저장
exit_order = []  # 나온 순서 저장

# 차량의 들어간 순서 저장
for i in range(n):
    car_num = input().strip()
    enter_order[car_num] = i

# 차량의 나온 순서 저장
exit_order = [input().strip() for _ in range(n)]

count = 0

# 나온 차량들을 확인하며 추월 여부 판단
for i in range(n - 1):
    for j in range(i + 1, n):
        if enter_order[exit_order[i]] > enter_order[exit_order[j]]:
            count += 1
            break

print(count)