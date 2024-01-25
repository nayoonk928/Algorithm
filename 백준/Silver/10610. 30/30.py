def find_largest_multiple_of_30(digits):
    # 모든 숫자의 합이 3의 배수인지 확인
    total_sum = sum(digits)
    if total_sum % 3 != 0:
        return -1

    # 0의 개수 확인
    zero_count = digits.count(0)

    # 만약 0이 하나도 없으면 30의 배수가 될 수 없음
    if zero_count == 0:
        return -1

    # 0이 있으면 0을 제외한 숫자들을 큰 순서대로 정렬
    non_zero_digits = sorted([d for d in digits if d != 0], reverse=True)

    # 숫자들을 이어붙이고 뒤에 0을 붙임
    result = int(''.join(map(str, non_zero_digits)) + '0' * zero_count)

    return result


if __name__ == "__main__":
    N = input().strip()

    # 입력받은 문자열을 숫자 리스트로 변환
    digits = [int(digit) for digit in N]

    result = find_largest_multiple_of_30(digits)
    print(result)