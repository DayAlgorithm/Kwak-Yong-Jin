import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
d = [[0] * (m) for _ in range(n)]
d[0][0] = graph[0][0]
for i in range(n):
    for j in range(m):
        if i+1 < n:
            d[i+1][j] = max(d[i+1][j], d[i][j] + graph[i+1][j])
        
        if j+1 < m:
            d[i][j+1] = max(d[i][j+1], d[i][j] + graph[i][j+1])
        
        if i+1 < n and j+1 < m:
            d[i+1][j+1] = max(d[i+1][j+1], d[i][j] + graph[i+1][j+1])
print(d[n-1][m-1])
