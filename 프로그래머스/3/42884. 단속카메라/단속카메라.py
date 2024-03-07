def solution(routes):
    # 차량의 이동 경로를 시작점을 기준으로 정렬
    routes.sort(key=lambda x: x[0])
    
    # 현재 카메라의 위치를 차량의 진출 지점으로 초기화
    camera_location = routes[0][1]
    
    # 설치된 카메라의 대수
    camera_count = 1
    
    # 모든 차량에 대해 순회
    for route in routes:
        # 현재 차량이 현재 카메라의 위치를 지나치지 않으면 새로운 카메라를 설치하고 위치 업데이트
        if route[0] > camera_location:
            camera_location = route[1]
            camera_count += 1
        # 현재 차량의 진출 지점이 현재 카메라의 위치보다 앞에 있으면 위치 업데이트
        elif route[1] < camera_location:
            camera_location = route[1]
    
    return camera_count