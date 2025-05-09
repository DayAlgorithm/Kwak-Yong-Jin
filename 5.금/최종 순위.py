import sys
from collections import deque
input = sys.stdin.readline

t = int(input()) 
for _ in range(t):
    n = int(input())
    last_year = list(map(int, input().split()))
    
    graph = [[False]*(n+1) for _ in range(n+1)] # 간선 여부 판단
    indegree = [0]*(n+1)
   
    for i in range(n):
        for j in range(i+1, n):
            graph[last_year[i]][last_year[j]] = True # 간선을 일단 받기
            indegree[last_year[j]] += 1

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        
        if graph[a][b]: # 간선 뒤집기
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1 # 계수도 뒤집기
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    # 위상정렬 시작
    q = deque()
    result = []
    for i in range(1, n+1):
        if indegree[i] == 0: 
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        if len(q) == 0:
            cycle = True
            break
        if len(q) > 1:
            certain = False
            break
        now = q.popleft()
        result.append(now)
        for j in range(1, n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        print(*result)
