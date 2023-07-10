def solution(my_string, letter):
    answer = "".join(filter(lambda x : x not in letter, my_string))
    return answer