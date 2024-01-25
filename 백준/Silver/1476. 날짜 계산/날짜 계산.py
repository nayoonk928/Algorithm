import sys
input = sys.stdin.readline


def find_year(e, s, m):
    year = 1

    while True:
        if (year - e) % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
            return year

        year += 1

if __name__ == "__main__":
    e, s, m = map(int, input().split())
    result = find_year(e, s, m)
    print(result)