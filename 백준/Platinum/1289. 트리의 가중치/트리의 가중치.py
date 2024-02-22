import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘립니다.

MOD = 10**9 + 7

def dfs(v, parent):
    global ans
    now = 1
    for nxt, w in graph[v]:
        if nxt != parent:
            t = dfs(nxt, v) * w % MOD
            ans += now * t % MOD
            ans %= MOD
            now += t
            now %= MOD
    return now

n = int(input())
graph = [[] for _ in range(n + 1)]
ans = 0

for _ in range(n - 1):
    s, e, x = map(int, input().split())
    graph[s].append((e, x))
    graph[e].append((s, x))

dfs(1, 0)
print(ans)
