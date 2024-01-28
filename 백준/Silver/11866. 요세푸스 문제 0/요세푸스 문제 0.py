import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())

    # 원형으로 앉은 사람들을 나타내는 리스트 생성
    people = list(range(1, N + 1))
    result = []

    # 현재 위치를 나타내는 변수
    current = 0

    while people:
        # K번째 사람을 제거하고 결과 리스트에 추가
        current = (current + K - 1) % len(people)
        result.append(people.pop(current))

    print("<" + ", ".join(map(str, result)) + ">")