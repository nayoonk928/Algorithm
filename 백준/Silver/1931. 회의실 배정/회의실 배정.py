import sys
input = sys.stdin.readline


def maximum_meetings(n, meetings):
    # 회의 끝나는 시간을 기준으로 정렬
    sorted_meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

    count = 1  # 첫 번째 회의는 항상 선택
    end_time = sorted_meetings[0][1]

    for i in range(1, n):
        start, end = sorted_meetings[i]
        if start >= end_time:
            count += 1
            end_time = end

    return count


if __name__ == "__main__":
    n = int(input())
    meetings = [tuple(map(int, input().split())) for _ in range(n)]

    result = maximum_meetings(n, meetings)
    print(result)
