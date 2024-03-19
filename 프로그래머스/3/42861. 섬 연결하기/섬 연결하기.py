def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, node1, node2):
    root1 = find(parent, node1)
    root2 = find(parent, node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def solution(n, costs):
    answer = 0
    # 각 섬의 부모 노드를 저장하는 배열
    parent = [i for i in range(n)]
    # 각 섬의 높이(랭크)를 저장하는 배열
    rank = [0] * n

    # 다리 건설 비용을 기준으로 costs를 정렬
    costs.sort(key=lambda x: x[2])

    for cost in costs:
        island1, island2, bridge_cost = cost
        # 사이클이 발생하지 않는다면(두 섬이 같은 그래프에 속하지 않는다면) 다리를 건설한다.
        if find(parent, island1) != find(parent, island2):
            union(parent, rank, island1, island2)
            answer += bridge_cost

    return answer