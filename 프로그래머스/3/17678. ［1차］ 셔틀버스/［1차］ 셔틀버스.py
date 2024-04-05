def time_to_minutes(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours * 60 + minutes

def solution(n, t, m, timetable):
    # timetable을 정렬
    timetable.sort(key=time_to_minutes)

    last_shuttle_time = 9 * 60 + (n - 1) * t  # 마지막 셔틀 운행 시간

    idx = 0  # timetable을 탐색할 인덱스
    for shuttle in range(n):
        shuttle_time = 9 * 60 + shuttle * t  # 셔틀 도착 시간
        count = 0  # 현재 셔틀에 탑승한 크루 수

        while idx < len(timetable) and time_to_minutes(timetable[idx]) <= shuttle_time:
            count += 1
            idx += 1

            if count == m:
                break

        if shuttle == n - 1:  # 마지막 셔틀 운행일 때
            if count < m:  # 자리가 남으면 셔틀 운행 시간에 도착
                answer = shuttle_time
            else:  # 자리가 없으면 가장 늦게 도착한 크루의 시간보다 1분 일찍 도착
                answer = time_to_minutes(timetable[idx - 1]) - 1

            if answer > last_shuttle_time:  # 마지막 셔틀 운행 시간 이후에 도착하는 경우
                answer = last_shuttle_time

    return '%02d:%02d' % (answer // 60, answer % 60)