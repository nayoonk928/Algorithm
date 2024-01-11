import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def dfs(node, visited):
    visited.append(node)

    for adj in sorted(graph[node]):
        if adj not in visited:
            dfs(adj, visited)

    return visited


def bfs(start):
    visited = [start]
    queue = deque([start])

    while queue:
        node = queue.popleft()
        for adj in sorted(graph[node]):
            if adj not in visited:
                queue.append(adj)
                visited.append(adj)

    return visited


if __name__ == "__main__":
    vertex, edge, start = map(int, input().split())
    graph = defaultdict(list)

    for i in range(edge):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    dfs_result = dfs(start, [])
    bfs_result = bfs(start)

    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))