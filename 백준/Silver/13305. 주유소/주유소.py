import sys
input = sys.stdin.readline

n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))

result = 0
curr_oil = 0
for idx, val in enumerate(distance):
    if curr_oil >= val:
        curr_oil -= val
    else:
        oil_idx = 0  # 지금보다 싼 주유소 인덱스
        for i in oil[idx:]:  # 지금보다 싼 주요소 위치 찾기
            if i < oil[idx]:
                oil_idx = oil.index(i)
                break
        if oil_idx == 0:  # 싼 곳이 없음
            curr_oil += oil[idx] * sum(distance[idx:])
            result += oil[idx] * sum(distance[idx:])
            break
        else:  # 싼 곳 있음, 그곳까지 갈 만큼만 구매
            curr_oil += sum(distance[idx:oil_idx])
            result += oil[idx] * sum(distance[idx:oil_idx])
            curr_oil -= val

print(result)
