import sys

input = sys.stdin.readline


def dfs(node):
    tree[node] = -2
    for i in range(n):
        if node == tree[i]:
            dfs(i)


if __name__ == "__main__":
    n = int(input())
    tree = list(map(int, input().split()))
    delete_node = int(input())

    dfs(delete_node)

    count = 0
    for i in range(n):
        if tree[i] != -2 and i not in tree:
            count += 1

    print(count)