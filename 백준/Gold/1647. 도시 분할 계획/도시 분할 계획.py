import sys

input = sys.stdin.readline


def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])

    return parent[vertex]


def union(a, b):
    a_parent = find(a)
    b_parent = find(b)

    parent[b_parent] = a_parent


def get_minimum_cost(edges):
    edges.sort(key=lambda x: x[2])
    total_cost = 0
    max_weight = 0

    for idx, adj, weight in edges:
        if find(idx) != find(adj):
            union(idx, adj)
            total_cost += weight
            max_weight = weight  # 가장 큰 가중치 = 마지막 가중치

    return total_cost - max_weight


if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    parent = [i for i in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        if a != b:
            edges.append((a, b, c))

    print(get_minimum_cost(edges))