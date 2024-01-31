def solution(my_string):
    # 알파벳 개수를 저장할 배열 초기화
    alphabet_count = [0] * 52

    # 문자열을 순회하며 알파벳 개수 카운트
    for char in my_string:
        # 대문자인 경우
        if 'A' <= char <= 'Z':
            alphabet_count[ord(char) - ord('A')] += 1
        # 소문자인 경우
        elif 'a' <= char <= 'z':
            alphabet_count[ord(char) - ord('a') + 26] += 1

    return alphabet_count