import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jewels.sort()
bags.sort()    

max_heap = []
result = 0
jewel_idx = 0

for bag in bags:
    
    while jewel_idx < N and jewels[jewel_idx][0] <= bag:
        
        heapq.heappush(max_heap, -jewels[jewel_idx][1])
        jewel_idx += 1
  
    if max_heap:
        result -= heapq.heappop(max_heap)

print(result)
