import sys
input = sys.stdin.readline

n = int(input())
data = [tuple(map(int, input().split())) for _ in range(n)]
data.sort()

total = sum(a for x, a in data)
cnt = 0

for x, a in data:
    cnt += a
    if cnt >= total / 2:
        print(x)
        break
