import heapq

def dijkstra(n, graph, start):
    # 출발 지점부터의 최단 거리를 저장할 리스트
    distances = [float('inf')] * (n + 1)
    distances[start] = 0
    
    # 우선순위 큐를 사용한 Dijkstra 알고리즘
    queue = []
    heapq.heappush(queue, (0, start))
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # 현재 노드까지의 거리가 기존에 저장된 거리보다 크다면 스킵
        if current_distance > distances[current_node]:
            continue
        
        # 현재 노드에서 이동 가능한 모든 인접 노드에 대해 최단 거리 갱신
        for adjacent, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))
    
    return distances

def solution(n, roads, sources, destination):
    # 인접 리스트 생성
    graph = [[] for _ in range(n + 1)]
    for road in roads:
        a, b = road
        graph[a].append((b, 1))  # 양방향이므로 (b, 1)과 (a, 1) 모두 추가
        graph[b].append((a, 1))
    
    # destination으로부터의 최단 거리 계산
    distances_to_destination = dijkstra(n, graph, destination)
    
    answer = []
    for source in sources:
        # 각 부대원의 위치로부터 destination까지의 최단 거리
        shortest_distance = distances_to_destination[source]
        if shortest_distance == float('inf'):  # 도달할 수 없는 경우
            answer.append(-1)
        else:
            answer.append(shortest_distance)
    
    return answer