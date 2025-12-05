import sys
from bisect import bisect_left

input = sys.stdin.readline

m, n, l = map(int, input().split())
hunters = list(map(int, input().split()))
hunters.sort()

ans = 0

for _ in range(n):
    x, y = map(int, input().split())
    
    if y > l:
        continue
        
    idx = bisect_left(hunters, x)
    
    if idx < m and abs(hunters[idx] - x) + y <= l:
        ans += 1
        continue
        
    if idx > 0 and abs(hunters[idx-1] - x) + y <= l:
        ans += 1

print(ans)
