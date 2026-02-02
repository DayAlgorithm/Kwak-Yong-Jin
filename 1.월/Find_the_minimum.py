import sys
from collections import deque
input = sys.stdin.readline

n, l = map(int, input().split())
a = list(map(int, input().split()))
d = deque()
for i in range(n):
    cur = a[i]

    while d and d[-1][1] > cur:
        d.pop()
    
    d.append((i, cur))
    
    if d[0][0] < i - l + 1:
        d.popleft()

    print(d[0][1], end=' ')
