# dict = {차량번호, [시간기록]} -> 인덱스 짝수 = IN, 홀수 = OUT
# dict에 시간 저장 시 분으로 변환하여 저장 ex) 01:34 -> 94
# 1. 기본시간 이하인 경우 기본요금 반환
# 2. 기본시간 초과인 경우 기본요금 + ((OUT - IN - 기본시간) / 단위시간) * 단위 요금
import collections
import math

def solution(fees, records):
    answer = []
    dict = collections.defaultdict(list)
    last_time = 23 * 60 + 59

    for record in records:
        r = record.split(" ")
        time = r[0].split(":")
        minutes = int(time[0]) * 60 + int(time[1])
        dict[r[1]].append(minutes)

    dict = sorted(dict.items())

    for times in dict:
        total_time = 0
        for idx in range(0, len(times[1]), 2):
            in_time = times[1][idx]
            out_time = times[1][idx + 1] if idx + 1 < len(times[1]) else last_time
            total_time += (out_time - in_time)
            
        answer.append(calculate_fee(fees, total_time))

    return answer

def calculate_fee(fees, total_time):
    if total_time <= fees[0]:
        return fees[1]
    else:
        return fees[1] + (math.ceil((total_time - fees[0]) / fees[2]) * fees[3])
    