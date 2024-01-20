import sys
import heapq

input = sys.stdin.readline


def shortest_path(start):
    dist = [int(1e9) for _ in range(V + 1)]
    dist[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        weight, curr = heapq.heappop(pq)

        for adj, w in graph[curr]:
            cost = weight + w
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(pq, (cost, adj))

    return dist


if __name__ == '__main__':
    V, E = map(int, input().split())
    K = int(input())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))

    result = shortest_path(K)

    for i in range(1, V + 1):
        if result[i] == int(1e9):
            print("INF")
        else:
            print(result[i])