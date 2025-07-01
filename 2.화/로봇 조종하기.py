import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1e9]*m for _ in range(n)]
dp[0][0] = graph[0][0]

for x in range(1, m):
    dp[0][x] = dp[0][x - 1] + graph[0][x]

for y in range(1, n):
    left = [-1e9] * m
    right = [-1e9] * m

    left[0] = dp[y-1][0] + graph[y][0]
    for x in range(1, m):
        left[x] = max(left[x-1], dp[y-1][x]) + graph[y][x]
    
    right[m-1] = dp[y-1][m-1] + graph[y][m-1]
    for x in range(m-2, -1, -1):
        right[x] = max(right[x+1], dp[y-1][x]) + graph[y][x]
    
    for x in range(m):
        dp[y][x] = max(left[x], right[x])

print(dp[n-1][m-1])
