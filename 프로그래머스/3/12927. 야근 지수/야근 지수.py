def solution(n, works):
    if sum(works) <= n:
        return 0
    
    works.sort(reverse=True)
    
    while n > 0:
        max_work = works[0]
        for i in range(len(works)):
            if works[i] < max_work:
                break
            works[i] -= 1
            n -= 1
            if n == 0:
                return sum(work ** 2 for work in works)
    
    return sum(work ** 2 for work in works)