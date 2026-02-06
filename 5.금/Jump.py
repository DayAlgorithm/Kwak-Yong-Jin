import sys
input = sys.stdin.readline

def dfs(x, y):
    if x == n - 1 and y == n - 1:
        return 1
    
    if d[x][y] != -1:
        return d[x][y]

    d[x][y] = 0
    for i in range(2):
        nx = x + dx[i]*graph[x][y]
        ny = y + dy[i]*graph[x][y]

        if 0 <= nx < n and 0 <= ny < n:
            d[x][y] += dfs(nx, ny)

    return d[x][y]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

d = [[-1 for _ in range(n)] for _ in range(n)]
dx = [1, 0]
dy = [0, 1]

print(dfs(0, 0))
