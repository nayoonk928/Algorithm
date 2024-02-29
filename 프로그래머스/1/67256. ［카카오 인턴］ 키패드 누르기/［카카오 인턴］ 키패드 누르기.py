def solution(numbers, hand):
    answer = ''
    keypad = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2),
        '*': (3, 0), 0: (3, 1), '#': (3, 2)  # '*'와 '#'을 키패드 좌표에 추가
    }
    left_hand = '*'  # 왼손의 초기 위치
    right_hand = '#'  # 오른손의 초기 위치

    for num in numbers:
        if num in [1, 4, 7]:  # 왼손으로 누를 숫자
            answer += 'L'
            left_hand = num
        elif num in [3, 6, 9]:  # 오른손으로 누를 숫자
            answer += 'R'
            right_hand = num
        else:  # 가운데 열 숫자는 거리 비교 후 누르기
            l_dist = abs(keypad[left_hand][0] - keypad[num][0]) + abs(keypad[left_hand][1] - keypad[num][1])
            r_dist = abs(keypad[right_hand][0] - keypad[num][0]) + abs(keypad[right_hand][1] - keypad[num][1])

            if l_dist < r_dist:  # 왼손이 더 가까운 경우
                answer += 'L'
                left_hand = num
            elif l_dist > r_dist:  # 오른손이 더 가까운 경우
                answer += 'R'
                right_hand = num
            else:  # 거리가 같을 경우
                if hand == 'left':  # 왼손잡이는 왼손으로 누름
                    answer += 'L'
                    left_hand = num
                else:  # 오른손잡이는 오른손으로 누름
                    answer += 'R'
                    right_hand = num

    return answer