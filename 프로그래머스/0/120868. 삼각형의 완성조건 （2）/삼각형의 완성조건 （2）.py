def solution(sides):
    a, b = sides
    min_side = abs(a - b) + 1
    max_side = a + b - 1
    return max_side - min_side + 1