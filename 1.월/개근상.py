import sys
input = sys.stdin.readline
N = int(input())
MOD = 1000000
dp = [[[0] * 3 for _ in range(2)] for _ in range(N + 1)]
dp[0][0][0] = 1

for i in range(N):
    for j in range(2):
        for k in range(3): 
            if dp[i][j][k] == 0:
                continue
            dp[i+1][j][0] = (dp[i+1][j][0] + dp[i][j][k]) % MOD
            if j < 1:
                dp[i+1][j+1][0] = (dp[i+1][j+1][0] + dp[i][j][k]) % MOD
            if k < 2:
                dp[i+1][j][k+1] = (dp[i+1][j][k+1] + dp[i][j][k]) % MOD
ans = 0
for j in range(2):
    for k in range(3):
        ans = (ans + dp[N][j][k]) % MOD
print(ans)
