n = int(input())
a = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

a_set = set(a)

for target in targets:
    if target in a_set:
        print(1)
    else:
        print(0)