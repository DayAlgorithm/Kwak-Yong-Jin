import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1

    if cnt[x][y] != -1:
        return cnt[x][y]

    cnt[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] < graph[x][y]:
                cnt[x][y] += dfs(nx, ny)
    
    return cnt[x][y]

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
cnt = [[-1 for _ in range(n)] for _ in range(m)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(dfs(0, 0))
