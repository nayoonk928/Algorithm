def solution(genres, plays):
    # 장르별로 노래를 그룹화
    genre_dict = {}
    for i in range(len(genres)):
        if genres[i] not in genre_dict:
            genre_dict[genres[i]] = [(i, plays[i])]
        else:
            genre_dict[genres[i]].append((i, plays[i]))
    
    # 재생 횟수에 따라 노래를 정렬하고, 장르별로 최대 2개씩 선택
    answer = []
    for genre in sorted(genre_dict.keys(), key=lambda x: sum(y[1] for y in genre_dict[x]), reverse=True):
        genre_dict[genre].sort(key=lambda x: (-x[1], x[0]))
        answer.extend([song[0] for song in genre_dict[genre][:2]])
    
    return answer