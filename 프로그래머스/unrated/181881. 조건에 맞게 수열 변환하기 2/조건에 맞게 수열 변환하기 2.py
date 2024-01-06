import numpy as np

def solution(arr):
    answer = 0
    arr = np.array(arr)
    
    while True:
        prev = np.array(arr)
        
        for idx, num in enumerate(arr):
            if num >= 50 and num % 2 == 0:
                arr[idx] = num / 2
            elif num < 50 and num % 2 == 1:
                arr[idx] = num * 2 + 1
                
        if np.array_equal(prev, arr):
            return answer
            
        answer += 1
    
    return answer