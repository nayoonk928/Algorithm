# 백준 1197번 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197

import sys

input = sys.stdin.readline


def find(vertex):
    if parent[vertex] != vertex:
        parent[vertex] = find(parent[vertex])

    return parent[vertex]


def union(a, b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent


def get_minimum_weight():
    edges.sort(key=lambda x: x[2])

    min_sum = 0
    used_edges = 0

    for idx, adj, weight in edges:
        if find(idx) != find(adj):
            union(idx, adj)
            min_sum += weight
            used_edges += 1

            if used_edges == v - 1:
                break

    return min_sum


if __name__ == '__main__':
    v, e = map(int, input().split())
    edges = []
    parent = [i for i in range(v + 1)]

    for _ in range(e):
        idx, adj, weight = map(int, input().split())
        edges.append((idx, adj, weight))

    print(get_minimum_weight())
