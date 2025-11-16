import sys
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))

dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
dist[0][1] = 0
flag = True

for i in range(1, n+1):
    stable = True
    for v in range(1, n+1):
        cost = INF
        for u, c in graph[v]:
            cost = min(cost, dist[i-1][u] + c)
        dist[i][v] = min(dist[i-1][v], cost)
        if dist[i][v] != dist[i-1][v]:
            stable = False
    if stable == True:
        flag = False
        for tmp in dist[i-1][2:]:
            if tmp == INF:
                print(-1)
            else:
                print(tmp)
        break

if flag:
    print(-1)
