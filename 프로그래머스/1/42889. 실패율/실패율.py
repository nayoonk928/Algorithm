# 실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
# N = 전체 스테이지 개수, stages = 사용자가 현재 멈춰있는 스테이지 번호담은 배열
# 실패율이 높은 스테이지부터 담은 배열 반환
# 스테이지에 도달한 플레이어 수 : 스테이지 1에 도달한 플레이어 수 = stages[i] >= 1
# 클리어하지 못한 플레이어 수 : stages[i] = 1

def solution(N, stages):
    failure_rate = []
    
    for i in range(1, N + 1):
        reach = len([s for s in stages if s >= i])
        fail = len([s for s in stages if s == i])
        if reach == 0:
            failure_rate.append(0)
        else:
            failure_rate.append(fail/reach)
    
    answer = [idx + 1 for idx, value in sorted(enumerate(failure_rate), key=lambda x:x[1], reverse=True)]
    
    return answer