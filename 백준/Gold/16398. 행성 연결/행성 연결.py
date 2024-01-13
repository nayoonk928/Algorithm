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


def get_minimum_cost(n, costs):
    costs.sort(key=lambda x: x[2])

    min_sum = 0
    used_edges = 0

    for idx, adj, cost in costs:
        if find(idx) != find(adj):
            union(idx, adj)
            min_sum += cost
            used_edges += 1

            if used_edges == n - 1:
                break

    return min_sum


if __name__ == '__main__':
    n = int(input())
    costs = []
    parent = [i for i in range(n)]

    for i in range(n):
        weights = list(map(int, input().split()))
        for j in range(n):
            if i != j:
                costs.append((i, j, weights[j]))

    print(get_minimum_cost(n, costs))