from collections import defaultdict
def solution(genres, plays):
    answer = []
    genre_repeat = defaultdict(int) # 각 장르별 재생 횟수
    genre_number = {key: [] for key in genres} # 장르에 속한 노래의 고유번호
    for i in range(len(plays)):
        genre = genres[i] # 해당 장르
        repeat = plays[i] # 재생 횟수

        genre_repeat[genre] += repeat # 장르별 재생 횟수
        genre_number[genre].append(i)
        
    genre_repeat = list(genre_repeat.items()) # (장르, 횟수)
    genre_repeat = sorted(genre_repeat, key=lambda x : -x[1])
    
    for i in range(len(genre_repeat)):
        g, c = genre_repeat[i]
        tmp = []
        for num in genre_number[g]:
            tmp.append((plays[num], num))
        
        tmp = sorted(tmp, key=lambda x : (-x[0], x[1]))
        
        if len(tmp) >= 2:
            answer.append(tmp[0][1])
            answer.append(tmp[1][1])
        else:
            answer.append(tmp[0][1])
        
    return answer
