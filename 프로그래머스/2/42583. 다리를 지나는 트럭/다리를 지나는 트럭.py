from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # 다리를 나타내는 큐 초기화
    total_weight = 0

    while bridge:
        time += 1
        total_weight -= bridge.popleft()  # 다리에서 나가는 트럭의 무게를 빼줌

        if truck_weights:
            if total_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                bridge.append(truck)
                total_weight += truck
            else:
                bridge.append(0)  # 트럭이 못올라가면 0을 추가

    return time