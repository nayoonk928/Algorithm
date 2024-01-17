import sys

input = sys.stdin.readline


if __name__ == '__main__':
    n = int(input())
    members = []

    for _ in range(n):
        members.append(list(input().strip().split(" ")))

    members.sort(key=lambda x: (int(x[0])))

    for i in range(n):
        print(members[i][0], members[i][1])