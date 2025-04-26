def solution(n, results):
    graph = [[0] * (n+1) for _ in range(n+1)]
    
    for win, lose in results: # 각 선수들 사이의 승패관계
        graph[win][lose] = 1
        graph[lose][win] = -1

    for k in range(1, n+1):  # 플로이드-워셜 알고리즘 : i와 j의 승패 관계를 k를 거쳐서 나타냄
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = -1
                if graph[i][k] == -1 and graph[k][j] == -1:
                    graph[i][j] = -1
                    graph[j][i] = 1
    answer = 0
    for i in range(1, n+1): # 모든 선수와으 승패 관계가 확실한 선수인 경우에만 answer += 1 해줌
        cnt = 0
        for j in range(1, n+1):
            if i == j:
                continue
            if graph[i][j] != 0:
                cnt += 1
        if cnt == n-1:
            answer += 1
    return answer
