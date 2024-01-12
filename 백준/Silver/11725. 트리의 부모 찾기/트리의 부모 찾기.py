import sys

input = sys.stdin.readline


def get_parents(tree, n):
    parents = [0] * (n + 1)
    visited = [False] * (n + 1)
    stack = [1]  # 시작 노드를 스택에 넣음

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            for child in tree[node]:
                if not visited[child]:
                    parents[child] = node
                    stack.append(child)

    return parents


if __name__ == "__main__":
    n = int(input())
    tree = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        a, b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)

    result = get_parents(tree, n)

    for i in range(2, n + 1):
        print(result[i])