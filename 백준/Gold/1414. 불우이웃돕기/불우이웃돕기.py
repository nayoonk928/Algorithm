import sys

input = sys.stdin.readline


def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])

    return parent[vertex]


def union(a, b):
    a_parent = find(a)
    b_parent = find(b)

    if a < b:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


# 전체 가중치의 합 - 최소 가중치
def kruskal():
    edges.sort(key=lambda x: x[2])
    length = 0

    for idx, adj, weight in edges:
        if weight == 0:
            continue

        if find(idx) != find(adj):
            union(idx, adj)
            length += weight

    return length


if __name__ == '__main__':
    n = int(input())
    graph = []
    parent = [i for i in range(n)]

    for _ in range(n):
        row = list(input().strip())
        graph.append(row)

    edges = []
    total_len = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '0':
                edges.append((i, j, 0))
            else:
                if 'a' <= graph[i][j] <= 'z':
                    length = ord(graph[i][j]) - ord('a') + 1
                    edges.append((i, j, length))
                    total_len += length
                else:
                    length = ord(graph[i][j]) - ord('A') + 27
                    edges.append((i, j, length))
                    total_len += length

    result = kruskal()

    # 모든 정점이 연결되어 있는지 확인
    is_connected = set(find(i) for i in range(n))

    if len(is_connected) == 1:
        print(total_len - result)
    else:
        print(-1)