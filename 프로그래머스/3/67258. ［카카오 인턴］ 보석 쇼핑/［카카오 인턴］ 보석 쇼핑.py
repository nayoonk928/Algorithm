def solution(gems):
    gem_types = len(set(gems))  # 보석의 종류 수
    gem_dict = {}  # 현재 구간에 있는 보석의 종류와 수
    answer = [0, len(gems) - 1]  # 반환할 구간의 시작과 끝 초기화
    start, end = 0, 0  # 투 포인터 초기화

    while end < len(gems):
        # 종료 포인터가 가리키는 보석을 구간에 포함시키기
        if gems[end] not in gem_dict:
            gem_dict[gems[end]] = 1
        else:
            gem_dict[gems[end]] += 1

        # 현재 구간에 모든 종류의 보석이 포함되었는지 확인
        while len(gem_dict) == gem_types:
            # 현재 구간이 더 짧은 경우, 결과 업데이트
            if end - start < answer[1] - answer[0]:
                answer = [start, end]
            
            # 시작 포인터를 이동시키며 구간 갱신
            gem_dict[gems[start]] -= 1
            if gem_dict[gems[start]] == 0:
                del gem_dict[gems[start]]
            start += 1
        
        # 종료 포인터 이동
        end += 1
    
    # 진열대 번호를 1부터 시작하도록 조정
    return [answer[0] + 1, answer[1] + 1]