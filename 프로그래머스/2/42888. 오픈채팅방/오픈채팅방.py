def solution(record):
    user_info = {}  # 유저 아이디와 닉네임을 저장하는 딕셔너리
    result = []  # 최종 메시지를 저장하는 리스트

    for rec in record:
        command, *rest = rec.split()

        if command == "Enter" or command == "Change":
            user_id, nickname = rest
            user_info[user_id] = nickname  # 유저 아이디와 닉네임을 업데이트

    for rec in record:
        command, *rest = rec.split()
        user_id = rest[0]

        if command == "Enter":
            result.append(f"{user_info[user_id]}님이 들어왔습니다.")
        elif command == "Leave":
            result.append(f"{user_info[user_id]}님이 나갔습니다.")

    return result