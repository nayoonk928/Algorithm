import sys

input = sys.stdin.readline


def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])

    return parent[vertex]


# union-by-rank 이용
def union(a, b):
    a_parent = find(a)
    b_parent = find(b)

    parent[b_parent] = a_parent


def get_max(edges):
    edges.sort(key=lambda x: x[2], reverse=True)
    result = []

    for idx, adj, weight in edges:
        if find(start) == find(end):
            break

        if find(idx) != find(adj):
            union(idx, adj)
            result.append(weight)

    if find(start) == find(end):
        return min(result)
    else:
        return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    start, end = map(int, input().split())
    edges = []
    parent = [i for i in range(n + 1)]

    for _ in range(m):
        h1, h2, weight = map(int, input().split())
        if h1 != h2:
            edges.append((h1, h2, weight))

    print(get_max(edges))
