from itertools import combinations
from collections import Counter

def solution(orders, course):
    result = []

    for course_size in course:
        temp = []
        for order in orders:
            # 현재 주문에서 가능한 모든 조합을 찾아 temp에 추가
            comb = combinations(sorted(order), course_size)
            temp.extend(comb)
        
        # 조합별 주문 횟수를 계산
        order_count = Counter(temp)
        
        # 가장 많이 주문된 조합 찾기
        if order_count:
            max_count = max(order_count.values())
            # 최소 2명 이상의 손님으로부터 주문된 경우만 고려
            result.extend([''.join(menu) for menu, count in order_count.items() if count == max_count and count > 1])

    # 사전 순으로 정렬하여 반환
    return sorted(result)