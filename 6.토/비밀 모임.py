import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a][b] = c
        graph[b][a] = c
    
    k = int(input())
    friends = list(map(int, input().split()))

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][k] and graph[k][j]:
                    if graph[i][j] == 0:
                        graph[i][j] = graph[i][k] + graph[k][j]
                    else:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for i in range(1, n+1):
        graph[i][i] = 0
    
    distance = [0] * (n+1)
    for i in range(1, n+1):
        for friend in friends:
            distance[i] += graph[friend][i]

    tmp = min(distance[1:])
    for i in range(1, n+1):
        if distance[i] == tmp:
            ans = i
            break
    print(ans)
