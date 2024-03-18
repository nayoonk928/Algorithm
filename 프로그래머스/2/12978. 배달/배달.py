from collections import defaultdict
import heapq

def solution(N, road, K):
    graph = defaultdict(list)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))
    
    distances = {node: float('inf') for node in range(1, N+1)}
    distances[1] = 0
    
    queue = [(0, 1)]
    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distances[node]:
            continue
        for neighbor, cost in graph[node]:
            new_dist = dist + cost
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(queue, (new_dist, neighbor))
    
    count = 0
    for dist in distances.values():
        if dist <= K:
            count += 1
    return count