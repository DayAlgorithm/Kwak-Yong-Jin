import sys
import heapq
input = sys.stdin.readline

N, M, K = map(int, input().split())
beers = []
for _ in range(K):
    v, c = map(int, input().split())
    beers.append((c, v)) 

beers.sort()   # 도수 순으로 정렬

heap = []
total = 0
answer = -1

for c, v in beers:
    heapq.heappush(heap, v)
    total += v

    if len(heap) > N:
        total -= heapq.heappop(heap)

    if len(heap) == N and total >= M:
        answer = c
        break 

print(answer)
