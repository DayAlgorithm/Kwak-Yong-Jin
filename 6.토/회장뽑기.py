import sys
input = sys.stdin.readline
INF = float('inf')

n = int(input())
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]
while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break

    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n+1):
    graph[i][i] = 1


for k in range(1, n+1): # 플로이드 워셜
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

result = [0]*(n+1)
score = INF
for i in range(1, n+1): # INF를 제외한 최장거리 기록
    tmp = 0
    for j in range(1, n+1):
        if graph[i][j] == INF:
            continue
        
        if graph[i][j] > tmp:
            tmp = graph[i][j]

    result[i] = tmp

    if tmp < score: # 뽑은 최장거리중 최단거리 기록
        score = tmp
        
cnt = 0
answer = []
for i in range(1, n+1): # 최단거리인 사람이 회장 후보
    if result[i] == score:
        cnt += 1
        answer.append(i)

answer.sort()

print(score, cnt)
print(*answer)
