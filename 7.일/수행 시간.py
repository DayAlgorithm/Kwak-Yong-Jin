import sys
input = sys.stdin.readline

n = int(input().strip())
ranks = [[] for _ in range(n + 1)]  
times = [0] * (n + 1)               

for i in range(1, n + 1):
    c, t = map(int, input().split())
    ranks[c].append(i)
    times[i] = t

dp = [0] * (n + 1)

for i in ranks[1]:
    dp[i] = times[i]

for r in range(2, n + 1):
    if not ranks[r]:
        continue

    for node in ranks[r]:
        best = 0
        for prev in ranks[r - 1]:
            cand = dp[prev] + (node - prev) ** 2
            if cand > best:
                best = cand
        dp[node] = best + times[node]

print(max(dp))
