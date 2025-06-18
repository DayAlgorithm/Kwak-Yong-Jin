import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [INF] * (n+1)
prev = [-1] * (n+1)
heap = []
dist[1] = 0
heap.append((0, 1)) # 누적 거리, 노드
prev[1] = 1


while heap:
    cost, cur = heapq.heappop(heap)
    if dist[cur] < cost:
        continue

    for nxt, nxtcost in graph[cur]:
        if dist[nxt] > dist[cur] + nxtcost:
            dist[nxt] = dist[cur] + nxtcost
            heapq.heappush(heap, (dist[nxt], nxt))
            prev[nxt] = cur

answer = set()
for i in range(2, n+1):
    recover = i
    route = [i]
    while prev[recover] != 1:
        route.append(prev[recover])
        recover = prev[recover]
    route.append(prev[recover])
    route.reverse()
    for j in range(len(route) - 1):
        answer.add((route[j], route[j+1]))

print(len(answer))
for result in answer:
    result = list(result)
    print(*result)
