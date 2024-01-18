import sys
input = sys.stdin.readline


def select():
    # 서류 기준으로 오름차순 정렬
    sorted_applicants = sorted(applicants, key=lambda x: x[0])

    result = 1
    doc = 1  # 서류 기준으로 오름차순 정렬을 했기 때문에 초기값 1
    interview = sorted_applicants[0][1]

    idx = 1
    while interview > 1:
        curr_interview = sorted_applicants[idx][1]
        if curr_interview < interview:
            interview = curr_interview
            result += 1
        idx += 1

    return result


if __name__ == '__main__':
    t = int(input())  # 테스트 케이스 개수

    for _ in range(t):
        n = int(input())  # 지원자 수
        applicants = []

        for _ in range(n):
            a, b = map(int, input().split())
            applicants.append((a, b))

        print(select())