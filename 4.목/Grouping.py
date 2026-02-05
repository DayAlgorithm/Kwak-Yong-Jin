import sys
input = sys.stdin.readline

n = int(input())
score = list(map(int, input().split()))
d = [0] * n
d[0] = 0

for i in range(1, n):
    tmp = 0
    for j in range(i, -1, -1):
        j_max = max(score[j:i+1])
        j_min = min(score[j:i+1])

        tmp = max(tmp, d[j-1] + abs(j_max - j_min))
    d[i] = tmp
print(d[n-1])
