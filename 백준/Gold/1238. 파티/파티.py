import sys
import heapq

input = sys.stdin.readline


def dijkstra(start):
    dist = [int(1e9) for _ in range(n + 1)]
    pq = []

    heapq.heappush(pq, (0, start))
    dist[start] = 0

    while pq:
        weight, curr = heapq.heappop(pq)

        if dist[curr] < weight:
            continue

        for adj, w in graph[curr]:
            cost = weight + w

            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(pq, (cost, adj))

    return dist


if __name__ == '__main__':
    # 학생 수, 도로 개수, 도착 노드
    n, m, x = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        start, end, weight = map(int, input().split())
        graph[start].append((end, weight))

    result = 0

    for i in range(1, n + 1):
        if i == x:
            continue

        from_home = dijkstra(i)
        to_party = dijkstra(x)

        total_time = from_home[x] + to_party[i]
        result = max(result, total_time)

    print(result)