def solution(new_id):
    # 1단계: 모든 대문자를 대응되는 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    allowed_chars = set("abcdefghijklmnopqrstuvwxyz0123456789-_.")
    new_id = ''.join(char for char in new_id if char in allowed_chars)
    
    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
        
    # 4단계: 마침표(.)가 처음이나 끝에 위치한다면 제거
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
        
    # 5단계: 빈 문자열이라면, new_id에 "a"를 대입
    if not new_id:
        new_id = 'a'
        
    # 6단계: 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    #        만약 제거 후 마침표(.)가 끝에 위치한다면 마침표(.) 문자 제거
    new_id = new_id[:15]
    if new_id.endswith('.'):
        new_id = new_id[:-1]
        
    # 7단계: 길이가 2자 이하라면, 마지막 문자를 길이가 3이 될 때까지 반복해서 끝에 붙임
    while len(new_id) < 3:
        new_id += new_id[-1]
        
    return new_id