def solution(sizes):    
    sorted_sizes = [sorted(sublist, key=lambda x: x, reverse=True) for sublist in sizes]
    
    max_first_element = max(sorted_sizes, key=lambda x: x[0])[0]
    max_second_element = max(sorted_sizes, key=lambda x: x[1])[1]
    
    return max_first_element * max_second_element