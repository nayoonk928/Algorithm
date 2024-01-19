import sys
input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())

start, end = 0, max(budgets)

while start <= end:
    mid = (start + end) // 2
    total = sum(min(budget, mid) for budget in budgets)

    if total <= total_budget:
        start = mid + 1
    else:
        end = mid - 1

print(end)