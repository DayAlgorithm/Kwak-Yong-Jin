import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    graph = list(map(int, input().split()))
    dic_score = {}
    dic_count = {}
    score = []
    cnt = 1
    for i in range(len(graph)):
        if graph.count(graph[i]) == 6: # 참가 선수가 6명 이상인 팀만 추출하기
            dic_score[graph[i]] = 0
            dic_count[graph[i]] = 0
            score.append([graph[i],cnt])
            cnt += 1

    for team, num in score: # 각 팀별 점수 계산하기
        if dic_count[team] < 4:
            dic_score[team] += num
            dic_count[team] += 1
    
    lst_score = list(sorted(dic_score.items(), key=lambda x: x[1]))
    _max = lst_score[0][1]

    tmp = [lst_score[0][0]]
    for i in range(1, len(lst_score)):
        if lst_score[i][1] == _max:
            tmp.append(lst_score[i][0])
    
    if len(tmp) == 1: # 동점이 없는 경우 우승 팀
        print(tmp[0])
        continue

    ret_team = {}
    ret_count = {}
    for i in range(len(tmp)): # 동점 생길 시 5번째로 들어온 선수들의 등수 비교
        ret_team[tmp[i]] = 0
        ret_count[tmp[i]] = 0

    for i in range(len(graph)):
        num = graph[i]
        if num in tmp and ret_count[num] < 5:
            ret_count[num] += 1
            ret_team[num] = i+1
    
    ret = list(sorted(ret_team.items(), key=lambda x: x[1]))
    print(ret[0][0])
