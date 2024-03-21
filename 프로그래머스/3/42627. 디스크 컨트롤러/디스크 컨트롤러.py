import heapq

def solution(jobs):
    # 작업 요청 시간에 따라 오름차순 정렬
    jobs.sort()
    # 대기중인 작업 목록
    wait_list = []
    # 현재 시간, 완료된 작업 수, 작업의 총 소요 시간
    current_time, completed_jobs, total_time = 0, 0, 0
    jobs_len = len(jobs)
    
    while completed_jobs < jobs_len:
        # 현재 시간 이전에 요청된 모든 작업을 대기 목록에 추가
        while jobs and jobs[0][0] <= current_time:
            request, duration = jobs.pop(0)
            heapq.heappush(wait_list, (duration, request))
        
        if wait_list:
            # 대기 목록에서 소요 시간이 가장 짧은 작업 처리
            duration, request = heapq.heappop(wait_list)
            current_time += duration  # 현재 시간 업데이트
            total_time += current_time - request  # 총 소요 시간 업데이트
            completed_jobs += 1  # 완료된 작업 수 업데이트
        else:
            # 대기 목록이 비어 있으면 현재 시간을 다음 작업의 요청 시간으로 설정
            current_time = jobs[0][0]
    
    return total_time // jobs_len  # 작업의 요청부터 종료까지 걸린 시간의 평균