import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
k = list(map(int, input().split()))
k.sort()
heap = []
cnt = 0
cur = 0

while True:
    if cnt == n:
        break
    
    while len(heap) != m and k:
        heapq.heappush(heap, [k.pop(), cur])
    
    if heap[0][0] + heap[0][1] == cur:
        while heap and heap[0][0] + heap[0][1] == cur:
            heapq.heappop(heap)
            cnt += 1
        
        for i in range(len(heap)):
            heap[0][0] = heap[0][0] + heap[0][1] - cur
            heap[0][1] = cur
        
    while len(heap) != m and k:
        heapq.heappush(heap, [k.pop(), cur])

    cur += 1

print(cur-1)
