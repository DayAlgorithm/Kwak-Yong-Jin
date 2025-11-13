import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

d = [[[0]*3 for _ in range(n)] for _ in range(n)]
d[0][1][0] = 1 

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            continue

        if j+1 < n and graph[i][j+1] == 0:
            d[i][j+1][0] += d[i][j][0] + d[i][j][1]

        if i+1 < n and graph[i+1][j] == 0:
            d[i+1][j][2] += d[i][j][2] + d[i][j][1]

        if i+1 < n and j+1 < n:
            if graph[i+1][j] == 0 and graph[i][j+1] == 0 and graph[i+1][j+1] == 0:
                d[i+1][j+1][1] += d[i][j][0] + d[i][j][1] + d[i][j][2]

print(sum(d[n-1][n-1]))
