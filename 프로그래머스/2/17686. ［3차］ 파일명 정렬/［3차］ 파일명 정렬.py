import re

def solution(files):
    def key_function(file):
        # 정규표현식을 사용하여 HEAD, NUMBER, TAIL을 추출
        head, number, tail = re.match(r'([a-zA-Z-.\s]+)(\d{1,5})(.*)', file).groups()
        return (head.lower(), int(number))

    # key_function을 기준으로 정렬
    sorted_files = sorted(files, key=key_function)

    return sorted_files