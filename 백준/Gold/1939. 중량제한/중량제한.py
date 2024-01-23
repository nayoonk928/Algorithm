import sys
from collections import deque

input = sys.stdin.readline


def bfs(mid):
    visited = [False] * (n + 1)
    q = deque([start])
    visited[start] = True

    while q:
        current_node = q.popleft()

        for next_node, weight in graph[current_node]:
            if not visited[next_node] and weight >= mid:
                visited[next_node] = True
                q.append(next_node)

    return visited[end]


def binary_search():
    start, end = 1, int(1e9)
    result = 0

    while start <= end:
        mid = (start + end) // 2

        if bfs(mid):
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))  # 양방향 그래프를 만들기 위해 추가

    start, end = map(int, input().split())

    print(binary_search())