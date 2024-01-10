import sys
from collections import defaultdict
input = sys.stdin.readline

computer_cnt = int(input())
n = int(input())

graph = defaultdict(list)
visited = [False] * (computer_cnt + 1)

for _ in range(n):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(count, node, visited):
    visited[node] = True

    for adj in graph[node]:
        if not visited[adj]:
            count = dfs(count + 1, adj, visited)

    return count


print(dfs(0, 1, visited))