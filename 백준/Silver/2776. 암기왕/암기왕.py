
import sys
input = sys.stdin.readline


def check_numbers(t, test_cases):
    results = []

    for _ in range(t):
        n, notebook1, m, notebook2 = test_cases[_]

        # 수첩1에 있는 숫자들을 set으로 변환
        set_notebook1 = set(notebook1)

        # 결과를 저장할 리스트
        result = []

        # 수첩2의 각 숫자에 대해 수첩1에 존재하는지 여부 확인
        for num in notebook2:
            if num in set_notebook1:
                result.append(1)
            else:
                result.append(0)

        results.append(result)

    return results

if __name__ == '__main__':
    t = int(input())  # 테스트케이스의 개수

    test_cases = []
    for _ in range(t):
        n = int(input())  # 수첩1에 적힌 정수의 개수
        notebook1 = list(map(int, input().split()))  # 수첩1에 적힌 정수들
        m = int(input())  # 수첩2에 적힌 정수의 개수
        notebook2 = list(map(int, input().split()))  # 수첩2에 적힌 정수들

        test_cases.append((n, notebook1, m, notebook2))

    results = check_numbers(t, test_cases)

    # 결과 출력
    for result in results:
        for num in result:
            print(num)