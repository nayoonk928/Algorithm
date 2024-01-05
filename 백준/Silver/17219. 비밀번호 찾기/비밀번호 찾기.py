import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().rstrip().split())
    dic = {}
    for _ in range(n):
        key, value = input().rstrip().split()
        dic[key] = value

    for _ in range(m):
        site = input().rstrip()
        if site in dic:
            print(dic[site])