import sys
input = sys.stdin.readline
MAX = float('inf')

N = int(input())
st1, st2 = sorted(map(int, input().split()))
T = int(input())
order = [int(input()) for _ in range(T)]

dp = [[[MAX]*(N+1) for _ in range(N+1)] for _ in range(T+1)]
dp[0][st1][st2] = 0 

for i in range(T):
    n = order[i]
    for st1 in range(1, N):
        for st2 in range(st1+1, N+1):
            if dp[i][st1][st2] == MAX:
                continue
            # f문을 n으로 이동
            if n < st2:
                dp[i+1][n][st2] = min(dp[i+1][n][st2], dp[i][st1][st2] + abs(st1 - n))
            # s문을 n으로 이동
            if n > st1:
                dp[i+1][st1][n] = min(dp[i+1][st1][n], dp[i][st1][st2] + abs(st2 - n))

print(min(map(min, dp[T]))) # 신기술
