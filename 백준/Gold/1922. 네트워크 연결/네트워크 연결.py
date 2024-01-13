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


def get_minimum_cost(n, edges):
    edges.sort(key=lambda x: x[2])
    min_cost = 0
    used_edges = 0

    for idx, adj, weight in edges:
        if find(idx) != find(adj):
            union(idx, adj)
            min_cost += weight
            used_edges += 1

            if used_edges == n - 1:
                break

    return min_cost


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    edges = []
    parent = [i for i in range(n + 1)]

    for i in range(m):
        a, b, c = map(int, input().split())
        if a != b:
            edges.append((a, b, c))

    print(get_minimum_cost(n, edges))