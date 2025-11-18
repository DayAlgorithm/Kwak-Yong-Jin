import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
numbers = graph[:-1]
target = graph[-1]

dp = [[0] * 21 for _ in range(n - 1)]
dp[0][numbers[0]] = 1

for i in range(1, n - 1):
    for j in range(21):
        if dp[i-1][j] > 0:
            add = j + numbers[i]
            if 0 <= add <= 20:
                dp[i][add] += dp[i-1][j]
            
            sub = j - numbers[i]
            if 0 <= sub <= 20:
                dp[i][sub] += dp[i-1][j]

print(dp[n-2][target])
