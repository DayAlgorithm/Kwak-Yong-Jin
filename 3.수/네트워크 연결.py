import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

visited = set()
heap = [(0, 1)]
answer = 0
while heap:
    c, cur = heapq.heappop(heap)
    if cur in visited:
        continue
    visited.add(cur)
    answer += c
    for nxt, cost in graph[cur]:
        heapq.heappush(heap, (cost, nxt))

print(answer)
