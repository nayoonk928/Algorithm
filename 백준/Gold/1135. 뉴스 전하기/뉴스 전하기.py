n = int(input())
emp = list(map(int, input().split()))
node = [[] for _ in range(n)]
child_cnt = [0 for _ in range(n)]

def go(x):
    global child_cnt
    child_node = []
    if not node[x]:
        child_cnt[x] = 0
    else:
        for child in node[x]:
            go(child)
            child_node.append(child_cnt[child])

        child_node.sort(reverse=True)
        child_node = [child_node[i] + i + 1 for i in range(len(child_node))]
        child_cnt[x] = max(child_node)

# 직원의 상사-직속부하 관계 설정
for i in range(1, len(emp)):
    node[emp[i]].append(i)

# 최대 깊이 구하기
go(0)

# 결과 출력
print(child_cnt[0])
