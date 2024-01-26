def solution(numlist, n):
    # numlist를 n으로부터의 거리와 크기를 기준으로 정렬
    sorted_list = sorted(numlist, key=lambda x: (abs(x - n), -x))
    return sorted_list