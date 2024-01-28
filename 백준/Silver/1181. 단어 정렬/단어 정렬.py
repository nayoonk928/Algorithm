import sys

input = sys.stdin.readline

if __name__ == '__main__':
    n = int(input())
    words = [input().strip() for _ in range(n)]

    words.sort(key=lambda x: (len(x), x))

    prev = ''
    for word in words:
        if word != prev:
            print(word)
            prev = word
