import sys

input = sys.stdin.readline


def get_parents(start):
    stack = [(start, 0)]  # (노드, 부모) 정보를 스택에 저장

    while stack:
        node, parent = stack.pop()

        parents[node] = parent

        for child in tree[node]:
            if parents[child] == 0:  # 방문하지 않은 노드일 경우에만 스택에 추가
                stack.append((child, node))

    return parents


if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    parents = [0] * (n + 1)
    result = get_parents(1)

    for i in range(2, n + 1):
        print(result[i])
