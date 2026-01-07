import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

for i in range(m):
    s, g = map(int, input().split())
    heap = [(0, s)]
    dist = [INF] * (n+1)
    dist[s] = 0

    while heap:
        cost, cur = heapq.heappop(heap)

        if cost > dist[cur]:
            continue

        for nxt, nxt_cost in graph[cur]:
            if dist[nxt] > cost + nxt_cost:
                dist[nxt] = cost + nxt_cost
                heapq.heappush(heap, (dist[nxt], nxt))
    
    print(dist[g])
