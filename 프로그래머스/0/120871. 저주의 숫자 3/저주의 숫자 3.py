def solution(n):
    # 3x 마을에서 사용하는 숫자를 저장할 리스트
    num_list = []
    current_number = 1
    
    # n개의 숫자를 찾을 때까지 반복
    while len(num_list) < n:
        # 3의 배수도 아니고 숫자 3이 포함되지 않은 경우
        if current_number % 3 != 0 and '3' not in str(current_number):
            num_list.append(current_number)
        # 다음 숫자로 이동
        current_number += 1
    
    # n번째 숫자 반환
    return num_list[n-1]