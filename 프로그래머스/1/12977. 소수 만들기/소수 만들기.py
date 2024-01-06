import itertools
import math

def solution(nums):
    answer = 0
    combinations = list(itertools.combinations(nums, 3))
    
    for c in combinations:
        if is_prime(sum(c)):
            answer += 1

    return answer

def is_prime(num):
    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    return True