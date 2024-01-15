import sys

input = sys.stdin.readline

def boy(swtich_num):
    for i in range(1, cnt + 1):
        if i % swtich_num == 0:
            switch[i] ^= 1  # 현재 비트 반전


def girl(switch_num):
    left, right = switch_num - 1, switch_num + 1

    while left >= 1 and right <= cnt and switch[left] == switch[right]:
        switch[left] ^= 1
        switch[right] ^= 1
        left -= 1
        right += 1

    switch[switch_num] ^= 1


if __name__ == '__main__':
    cnt = int(input())
    line = list(map(int, input().split()))
    switch = [0] + line  # 스위치 인덱스를 1부터 사용하기 위해 맨 앞에 0 추가

    stu_cnt = int(input())
    stu_info = []
    for _ in range(stu_cnt):
        stu_info.append(list(map(int, input().split())))

    for s in stu_info:
        gender, switch_num = s
        if gender == 1:
            boy(switch_num)
        else:
            girl(switch_num)

    for i in range(1, cnt + 1):
        print(switch[i], end=" ")
        if i % 20 == 0:
            print()