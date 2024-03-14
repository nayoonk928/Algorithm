def solution(n, wires):
    from collections import defaultdict

    # 인접 리스트를 생성하는 함수
    def create_graph(wires):
        graph = defaultdict(list)
        for v1, v2 in wires:
            graph[v1].append(v2)
            graph[v2].append(v1)
        return graph

    # DFS를 사용해 서브트리의 노드 개수를 계산하는 함수
    def dfs(graph, start, visited):
        count = 1
        visited[start] = True
        for node in graph[start]:
            if not visited[node]:
                count += dfs(graph, node, visited)
        return count

    # 최소 노드 차이를 초기화(최대값으로)
    min_diff = n
    for v1, v2 in wires:
        # 그래프 생성
        graph = create_graph(wires)
        # 간선 제거
        graph[v1].remove(v2)
        graph[v2].remove(v1)

        visited = [False] * (n + 1)
        # DFS 실행하여 한 쪽 서브트리의 노드 개수를 계산
        subtree_nodes = dfs(graph, v1, visited)
        # 두 서브트리의 노드 개수 차이를 계산
        min_diff = min(min_diff, abs(n - 2 * subtree_nodes))

    return min_diff