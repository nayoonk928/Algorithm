import sys

input = sys.stdin.readline    


t = int(input())

for _ in range(t):
    n = int(input())
    phone_nums = [input().strip() for _ in range(n)]
    
    phone_nums.sort()
    is_valid = True
    for i in range(n - 1):
        if phone_nums[i] == phone_nums[i + 1][:len(phone_nums[i])]:
            is_valid = False
            print("NO")
            break
    
    if is_valid:
        print("YES")