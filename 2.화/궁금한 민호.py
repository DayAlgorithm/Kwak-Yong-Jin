import sys
input = sys.stdin.readline

N = int(input())
dist = [list(map(int, input().split())) for _ in range(N)]

graph = [[True]*N for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j or i == k or j == k:
                continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                print(-1)
                sys.exit(0)
            if dist[i][j] == dist[i][k] + dist[k][j]:
                graph[i][j] = False
                graph[j][i] = False

answer = 0
for i in range(N):
    for j in range(i+1, N):
        if graph[i][j]:
            answer += dist[i][j]

print(answer)
