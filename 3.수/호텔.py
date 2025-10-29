import sys
input = sys.stdin.readline
INF = float('inf')

C, N = map(int, input().split())
cities = [tuple(map(int, input().split())) for _ in range(N)]
dp = [INF] * (C + 101) 
dp[0] = 0

for cost, people in cities:
    for j in range(people, C + 101):
        dp[j] = min(dp[j], dp[j - people] + cost)

print(min(dp[C:]))
