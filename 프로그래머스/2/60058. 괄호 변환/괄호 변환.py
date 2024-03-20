def solution(p):
    # 균형잡힌 괄호 문자열인지 확인하는 함수
    def is_balanced(s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
        return count == 0
    
    # 올바른 괄호 문자열인지 확인하는 함수
    def is_correct(s):
        stack = []
        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        return len(stack) == 0
    
    # 주어진 알고리즘에 따라 괄호 문자열을 변환하는 함수
    def convert(s):
        if s == '':
            return ''
        
        u, v = '', ''
        for i in range(2, len(s) + 1, 2):
            if is_balanced(s[:i]):
                u, v = s[:i], s[i:]
                break
        
        if is_correct(u):
            return u + convert(v)
        else:
            new_str = '(' + convert(v) + ')'
            for char in u[1:-1]:
                if char == '(':
                    new_str += ')'
                else:
                    new_str += '('
            return new_str
    
    return convert(p)