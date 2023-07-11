def solution(num_list):
    odd = ''
    even = ''
    for i in range(len(num_list)):
        temp = num_list[i]
        if temp % 2 == 0:
            even += str(temp)
        else:
            odd += str(temp)
    return int(odd) + int(even)