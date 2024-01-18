import sys

input = sys.stdin.readline

def get_length():
    sensors.sort()

    if n == 1:
        return 0

    diffs = [sensors[i+1] - sensors[i] for i in range(n-1)]
    diffs.sort(reverse=True)

    return sum(diffs[k-1:])

if __name__ == '__main__':
    n = int(input())
    k = int(input()) 
    sensors = list(map(int, input().split()))

    print(get_length())
