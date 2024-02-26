import sys
from collections import deque

def find_cities_with_shortest_distance(N, M, K, X, roads):
    graph = [[] for _ in range(N + 1)]
    for road in roads:
        a, b = road
        graph[a].append(b)
    
    distances = [-1] * (N + 1)
    distances[X] = 0
    
    queue = deque([X])
    while queue:
        current = queue.popleft()
        for next_city in graph[current]:
            if distances[next_city] == -1:
                distances[next_city] = distances[current] + 1
                queue.append(next_city)
    
    result = []
    for city in range(1, N + 1):
        if distances[city] == K:
            result.append(city)
    
    return result

if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    roads = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
    
    answer = find_cities_with_shortest_distance(N, M, K, X, roads)
    if not answer:
        print(-1)
    else:
        for city in answer:
            print(city)
