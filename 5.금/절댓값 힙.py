import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
heap = []
chk = defaultdict(int)
for i in range(n):
    tmp = int(input())
    
    if tmp == 0:
        if not heap:
            print(0)
            continue
        
        cur = heapq.heappop(heap)
        if chk[-cur]:
            print(-cur)
            chk[-cur] -= 1
        
        else:
            print(cur)
            chk[cur] -= 1
    
    else:
        chk[tmp] += 1
        heapq.heappush(heap, abs(tmp))
