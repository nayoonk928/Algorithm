from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]  # 각 노드에 연결된 노드를 저장할 리스트
    distance = [-1] * (n + 1)  # 각 노드의 최단 거리를 저장할 리스트, -1로 초기화
    distance[1] = 0  # 시작 노드의 거리는 0

    # 그래프 정보 입력
    for e in edge:
        a, b = e
        graph[a].append(b)
        graph[b].append(a)
    
    # BFS
    queue = deque([1])
    while queue:
        current_node = queue.popleft()
        
        for next_node in graph[current_node]:
            if distance[next_node] == -1:  # 방문하지 않은 노드인 경우
                distance[next_node] = distance[current_node] + 1
                queue.append(next_node)
    
    max_distance = max(distance)
    return distance.count(max_distance)