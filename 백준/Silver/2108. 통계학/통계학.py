import collections
import sys

input = sys.stdin.readline

def get_mode(nums_dict):
    max_val = max(nums_dict.values())

    max_keys = []
    for key, value in nums_dict.items():
        if value == max_val:
            max_keys.append(key)

    if len(max_keys) > 1:
        return sorted(max_keys)[1]

    return max_keys[0]


if __name__ == '__main__':
    n = int(input())  # 홀수

    nums = []
    nums_dict = collections.defaultdict(int)
    total = 0
    for _ in range(n):
        num = int(input())
        total += num
        nums_dict[num] += 1
        nums.append(num)

    length = len(nums)
    # 평균
    print(round(total / length))

    nums = sorted(nums)
    # 중앙값
    print(nums[length // 2])

    # 최빈값 (여러 개 있을 때는 최빈값 중 두 번째로 작은 값)
    print(get_mode(nums_dict))

    # 범위 (최댓값과 최솟값의 차이)
    print(nums[-1] - nums[0])