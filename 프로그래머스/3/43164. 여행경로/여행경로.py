def solution(tickets):
    answer = []
    graph = {}
    
    # 그래프 생성
    for start, end in tickets:
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]
    
    # 출발지를 기준으로 정렬하여 DFS 탐색
    for key in graph:
        graph[key].sort(reverse=True)
        
    stack = ["ICN"]
    while stack:
        current = stack[-1]
        # 만약 해당 공항에서 출발하는 티켓이 없거나 이미 모든 티켓을 사용한 경우, 경로에 추가하고 스택에서 제거
        if current not in graph or len(graph[current]) == 0:
            answer.append(stack.pop())
        else:
            # 스택의 최상단에 있는 도착 공항으로 가는 티켓을 사용하여 다음 공항으로 이동
            stack.append(graph[current].pop())
    
    # 경로를 역순으로 저장했으므로 다시 뒤집어서 반환
    return answer[::-1]