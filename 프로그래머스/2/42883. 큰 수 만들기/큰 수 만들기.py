def solution(number, k):
    stack = []  # 가장 큰 수를 만들기 위해 사용할 스택

    for num in number:
        # 스택이 비어있지 않고, 현재 숫자가 스택의 top보다 크고 아직 제거할 수가 남아있을 경우
        while stack and num > stack[-1] and k > 0:
            stack.pop()  # 스택의 top을 제거하여 큰 수를 만들어나감
            k -= 1

        stack.append(num)  # 현재 숫자를 스택에 추가

    # 만약 숫자를 모두 사용하지 않고도 k개의 수를 제거해야 하는 경우, 나머지 숫자를 제거
    while k > 0:
        stack.pop()
        k -= 1

    answer = ''.join(stack)
    return answer