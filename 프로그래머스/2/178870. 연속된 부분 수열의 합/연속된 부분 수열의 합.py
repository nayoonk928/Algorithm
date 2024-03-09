def solution(sequence, k):
    start, end = 0, 0
    curr_sum = 0
    min_length = float('inf')
    answer = []
    
    while end <= len(sequence):
        if curr_sum < k and end < len(sequence):
            curr_sum += sequence[end]
            end += 1
        elif curr_sum >= k:
            if curr_sum == k and (end - start) < min_length:
                min_length = end - start
                answer = [start, end - 1]
            curr_sum -= sequence[start]
            start += 1
        else:
            break
    
    return answer