import sys
input = sys.stdin.readline

n, t = map(int, input().split())
dp = [0] * (t + 1)

for _ in range(n):
    k, s = map(int, input().split())
    for j in range(t, k - 1, -1):
        dp[j] = max(dp[j], dp[j - k] + s)

print(dp[t])

