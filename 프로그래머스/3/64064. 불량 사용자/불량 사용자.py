def is_match(user_id, banned_id):
    if len(user_id) != len(banned_id):
        return False
    for i in range(len(user_id)):
        if banned_id[i] != '*' and user_id[i] != banned_id[i]:
            return False
    return True

def backtrack(users, banned_ids, idx, selected, result):
    if idx == len(banned_ids):
        result.add(tuple(sorted(selected)))  # 중복 제거를 위해 tuple로 변환하여 추가
        return
    
    for user in users:
        if user not in selected and is_match(user, banned_ids[idx]):
            selected.append(user)
            backtrack(users, banned_ids, idx + 1, selected, result)
            selected.pop()

def solution(user_id, banned_id):
    result = set()
    backtrack(user_id, banned_id, 0, [], result)
    return len(result)