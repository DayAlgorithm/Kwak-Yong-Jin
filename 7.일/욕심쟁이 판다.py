import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def dfs(y, x):
    if dp[y][x]:
        return dp[y][x]
    
    dp[y][x] = 1 
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < n:
            if graph[ny][nx] > graph[y][x]:
                dp[y][x] = max(dp[y][x], dfs(ny, nx) + 1)
    return dp[y][x]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)
