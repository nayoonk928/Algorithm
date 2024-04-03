from math import gcd
from functools import reduce

def find_gcd(list):
    x = reduce(gcd, list)
    return x

def solution(arrayA, arrayB):
    gcdA = find_gcd(arrayA)
    gcdB = find_gcd(arrayB)

    for b in arrayB:
        if b % gcdA == 0:
            gcdA = 0
            break
    
    for a in arrayA:
        if a % gcdB == 0:
            gcdB = 0
            break
    
    return max(gcdA, gcdB)