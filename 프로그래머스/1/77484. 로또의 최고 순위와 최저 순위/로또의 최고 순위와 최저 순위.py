# 알아 볼 수 없는 번호 = 0
# lottos = 구매한 번호 배열, win_nums = 당첨 번호 배열
# 0을 제외한 나머지 번호 중 당첨 번호와 맞는 번호가 몇 개인지 확인
# 0의 자리에 모두 당첨 번호가 들어간 경우 -> 최고 순위
# 0의 자리에 모두 낙첨 번호가 들어간 경우 -> 최저 순위

def solution(lottos, win_nums):
    answer = []
    common_count = 0
    count_zero = lottos.count(0)
    
    for num in lottos: 
        if num in win_nums:
            common_count += 1
    
    answer.append(rank(count_zero + common_count))
    answer.append(rank(common_count))
    
    return answer

def rank(match):
    if match == 6:
        return 1
    elif match == 5:
        return 2
    elif match == 4:
        return 3
    elif match == 3:
        return 4
    elif match == 2:
        return 5
    else:
        return 6