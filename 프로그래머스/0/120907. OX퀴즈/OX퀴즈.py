def solution(quiz):
    result = []
    
    for expression in quiz:
        x, operator, y, equal, z = expression.split()
        x, y, z = int(x), int(y), int(z)
        
        if operator == '+':
            if x + y == z:
                result.append("O")
            else:
                result.append("X")
        elif operator == '-':
            if x - y == z:
                result.append("O")
            else:
                result.append("X")
    
    return result