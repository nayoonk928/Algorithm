import sys

input = sys.stdin.readline

if __name__ == "__main__":
    # 집합 S의 문자열을 set으로 저장
    N, M = map(int, input().split())
    set_S = set(input().strip() for _ in range(N))

    # 검사해야 하는 문자열 중 집합 S에 속하는 개수 세기
    count = sum(1 for _ in range(M) if input().strip() in set_S)

    # 결과 출력
    print(count)