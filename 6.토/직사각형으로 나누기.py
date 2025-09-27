import sys
input = sys.stdin.readline

def presum(x1, y1, x2, y2):
    if x1 > x2 or y1 > y2:
        return 0
    return dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]

n, m = map(int, input().split())
graph = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1, n+1):
    lst = input().rstrip()
    for j in range(1, m+1):
        graph[i][j] = int(lst[j-1])
        dp[i][j] = graph[i][j] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

answer = 0

# 세로 3등분
for i in range(1, m-1):        # <= m-2
    for j in range(i+1, m):    # <= m-1
        r1 = presum(1, 1, n, i)
        r2 = presum(1, i+1, n, j)
        r3 = presum(1, j+1, n, m)
        answer = max(answer, r1 * r2 * r3)

# 가로 3등분
for i in range(1, n-1):        # <= n-2
    for j in range(i+1, n):    # <= n-1
        r1 = presum(1, 1, i, m)
        r2 = presum(i+1, 1, j, m)
        r3 = presum(j+1, 1, n, m)
        answer = max(answer, r1 * r2 * r3)

# 가로 2등분 후 세로 1등분
for i in range(1, m):          # <= m-1
    for j in range(1, n):      # <= n-1
        r1 = presum(1, 1, n, i)
        r2 = presum(1, i+1, j, m)
        r3 = presum(j+1, i+1, n, m)
        answer = max(answer, r1 * r2 * r3)

# 세로 2등분 후 가로 1등분
for i in range(1, n):          # <= n-1
    for j in range(1, m):      # <= m-1
        r1 = presum(1, 1, i, m)
        r2 = presum(i+1, 1, n, j)
        r3 = presum(i+1, j+1, n, m)
        answer = max(answer, r1 * r2 * r3)

# 가운데 세로 1등분 후 양옆 가로 1등분
for i in range(1, m):          # <= m-1
    for j in range(1, n):      # <= n-1
        r1 = presum(1, 1, j, i)
        r2 = presum(j+1, 1, n, i)
        r3 = presum(1, i+1, n, m)
        answer = max(answer, r1 * r2 * r3)

# 가운데 가로 1등분 후 양옆 세로 1등분
for i in range(1, n):          # <= n-1
    for j in range(1, m):      # <= m-1
        r1 = presum(1, 1, i, j)
        r2 = presum(1, j+1, i, m)
        r3 = presum(i+1, 1, n, m)
        answer = max(answer, r1 * r2 * r3)

print(answer)
