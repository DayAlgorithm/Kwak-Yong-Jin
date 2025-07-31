import sys
from collections import Counter

input = sys.stdin.readline
n, m = map(int, input().split())
rows = [input().strip() for _ in range(n)]
k = int(input())

counter = Counter(rows)
answer = 0
for pattern, count in counter.items():
    zero_count = pattern.count('0')
    if zero_count <= k and zero_count % 2 == k % 2:
        answer = max(answer, count)

print(answer)
