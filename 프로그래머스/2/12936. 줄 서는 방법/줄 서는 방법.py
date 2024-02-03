from math import factorial

def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))

    k -= 1

    for i in range(n, 0, -1):
        fact = factorial(i - 1)
        index = k // fact
        answer.append(numbers.pop(index))
        k %= fact

    return answer