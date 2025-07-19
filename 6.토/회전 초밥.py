import sys
from collections import defaultdict
input = sys.stdin.readline

n, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(n)]

counter = defaultdict(int)
max_kind = 0

for i in range(k):
    counter[sushi[i]] += 1

counter[c] += 1
max_kind = len(counter)

for i in range(1, n):
    prev = sushi[i - 1]
    counter[prev] -= 1
    if counter[prev] == 0:
        del counter[prev]

    nxt = sushi[(i + k - 1) % n]
    counter[nxt] += 1

    max_kind = max(max_kind, len(counter))

print(max_kind)
