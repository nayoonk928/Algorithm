# dart 점수 넣을 리스트 필요 -> score
# 보너스를 위한 dict 변수 필요 -> bonus
# 1. 숫자가 나오면 변수 num에 저장
# 2. 이후 나오는 문자에 따라 1에서 저장한 num에 곱하기
# 3. 옵션(*, #)이 나오면 index, index - 1 에 옵션에 맞게 값 적용
import math

def solution(dartResult):
    score = []
    bonus = {"S": 1, "D": 2, "T": 3}
    options = {"*": 2, "#": -1}
    current_num_str = ""
    for char in dartResult:
        if char.isnumeric():
            current_num_str += char
        elif char in bonus:
            current_num = int(current_num_str) ** bonus[char]
            score.append(current_num)
            current_num_str = ""
        else:
            length = len(score)
            if char == "*":
                if length == 1:
                    score[length - 1] *= 2
                elif length >= 2:
                    score[length - 2] *= 2
                    score[length - 1] *= 2
            elif char == "#":
                score[length - 1] *= -1
                
    return int(sum(score))