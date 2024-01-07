def solution(str_list):
    
    for char in str_list:
        if char == "l":
            index_l = str_list.index("l")
            left_list = str_list[:index_l]
            return left_list
        elif char == "r":
            index_r = str_list.index("r")
            right_list = str_list[index_r + 1:]
            return right_list
    
    return []