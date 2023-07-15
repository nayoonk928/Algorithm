def solution(emergency):
    answer = []
    count = 1
    
    for i in range(len(emergency)):
        for j in range(len(emergency)):
            if emergency[i] < emergency[j]:
                count += 1
        answer.insert(i, count)
        count = 1
    return answer