# 입력 받기
N = int(input())
numbers = [int(input()) for _ in range(N)]

# 오름차순 정렬
sorted_numbers = sorted(numbers)

# 정렬된 결과 출력
for num in sorted_numbers:
    print(num)