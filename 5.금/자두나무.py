import sys
input = sys.stdin.readline

t, w = map(int, input().split()) # 움직이는 횟수
graph = [int(input()) for _ in range(t)]

dp = [[0] * (w + 1) for _ in range(t)]
# dp[i][j] : i초에 j번 움직였을 때 얻을 수 있는 최대 갯수

for i in range(t):
    for j in range(w+1):
        if i == 0:
            if j % 2 == graph[i] - 1: # 1번 나무에 있을 때
                dp[i][j] = 1
            else:
                dp[i][j] = 0
            continue

        if j == 0: # 움직이지 않았을 때
            if graph[i] == 1:
                dp[i][j] = dp[i-1][j] + 1
            else:
                dp[i][j] = dp[i-1][j]
            continue

        if j % 2 == graph[i] - 1: # 1번 나무에 있을 때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        else: # 2번 나무에 있을 때
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])
print(max(dp[-1]))
