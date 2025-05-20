import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
m = int(input())
graph = [[INF] * (n+1) for _ in range(n+1)]
rot = [[0] * (n+1) for _ in range(n+1)]

def recoverpath(i, j): # 경로 복원 함수
    if i == j or graph[i][j] == INF:
        return []
    path = []
    while i != j:
        path.append(i)
        i = rot[i][j]
    path.append(j)

    return path

for _ in range(m):
    src, des, cost = map(int, input().split())
    if graph[src][des] > cost:
        graph[src][des] = cost
        rot[src][des] = des # 경로 복원 배열

for i in range(1, n+1): # 자기 자신이면 0
    graph[i][i] = 0

for k in range(1, n+1): # 플로이드 워셜
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][k] + graph[k][j] < graph[i][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                rot[i][j] = rot[i][k] # 경로 저장하는 배열

for i in range(1, n+1): # 최단경로가 적힌 graph 출력
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end = ' ')
    print()

for i in range(1, n+1): # 경로 복원해서 출력
    for j in range(1, n+1):
        if i == j or graph[i][j] == INF:
            print(0)
            continue
        result = recoverpath(i, j)
        print(len(result), *result)

            
