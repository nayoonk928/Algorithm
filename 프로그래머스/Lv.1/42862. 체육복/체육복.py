def solution(n, lost, reserve):
    lost.sort()
    
    # 여벌 체육복을 가져온 학생 중 도난당한 학생 제외
    real_reserve = [r for r in reserve if r not in lost]
    real_lost = [l for l in lost if l not in reserve]
    real_lost_cnt = len(real_lost)

    for l in real_lost:
        # 앞 뒤 학생에게 체육복을 빌려줄 수 있는지 확인
        if l - 1 in real_reserve:
            real_reserve.remove(l - 1)
            real_lost_cnt -= 1
        elif l + 1 in real_reserve:
            real_reserve.remove(l + 1)
            real_lost_cnt -= 1

    # 최종적으로 체육수업을 들을 수 있는 학생 수
    answer = n - real_lost_cnt
    
    return answer

