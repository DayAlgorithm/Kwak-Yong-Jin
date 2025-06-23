import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
d = [0] * (n+1)
for i in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
    indegree[e] += 1

queue = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)
        d[i] = 0

order = []
while queue:
    cur = queue.popleft()
    order.append(cur)
    for nxt, cost in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            queue.append(nxt)
    
for u in order:
    for v, w in graph[u]:
        tmp = 0
        if w >= 7:
            tmp = 1
        d[v] = max(d[v], d[u] + w + tmp)
    
print(max(d) + 1)
