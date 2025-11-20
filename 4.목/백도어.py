import sys
import heapq

# 빠른 입출력을 위해 설정
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())

vision = list(map(int, input().split()))

vision[n-1] = 0

graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append((b, t))
    graph[b].append((a, t))
    
dist = [INF] * n
dist[0] = 0
heap = []

heapq.heappush(heap, (0, 0))

while heap:
    cur_cost, cur = heapq.heappop(heap)
    
    if dist[cur] < cur_cost:
        continue
        
    for nxt, nxt_cost in graph[cur]:
        if vision[nxt] == 1:
            continue
            
        new_time = cur_cost + nxt_cost
        
        if new_time < dist[nxt]:
            dist[nxt] = new_time
            heapq.heappush(heap, (new_time, nxt))

if dist[n-1] == INF:
    print(-1)
else:
    print(dist[n-1])
