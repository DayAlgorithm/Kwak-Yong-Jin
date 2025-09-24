import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

heap = [(0, 2)]
dist = [float('inf')] * (n+1)
dist[2] = 0

while heap:
    cost, node = heapq.heappop(heap)
    if dist[node] < cost:
        continue
    for next_node, next_cost in graph[node]:
        new_cost = cost + next_cost
        if new_cost < dist[next_node]:
            dist[next_node] = new_cost
            heapq.heappush(heap, (new_cost, next_node))

dp = [-1] * (n+1)

def dfs(node, end):
    if node == end:
        return 1
    if dp[node] != -1:
        return dp[node]

    total = 0
    for nxt, _ in graph[node]:
        if dist[node] > dist[nxt]:
            total += dfs(nxt, end)
    
    dp[node] = total
    return total

print(dfs(1, 2))
