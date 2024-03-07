import sys
sys.setrecursionlimit(10**6)  # 재귀 깊이 제한을 늘려줍니다.

def count_subtree_nodes(cur):
    vis[cur] = True
    subtree_size[cur] = 1
    for nxt in adj[cur]:
        if not vis[nxt]:
            subtree_size[cur] += count_subtree_nodes(nxt)
    return subtree_size[cur]

N, R, Q = map(int, sys.stdin.readline().split())
adj = [[] for _ in range(N + 1)]
subtree_size = [0] * (N + 1)
vis = [False] * (N + 1)

for _ in range(N - 1):
    U, V = map(int, sys.stdin.readline().split())
    adj[U].append(V)
    adj[V].append(U)

count_subtree_nodes(R)

for _ in range(Q):
    q = int(sys.stdin.readline())
    print(subtree_size[q])
