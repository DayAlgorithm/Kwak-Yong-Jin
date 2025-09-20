import sys
from collections import deque
input = sys.stdin.readline

n, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    queue = deque()
    queue.append((i, float('inf')))
    visited = [False] * (n + 1)
    visited[i] = True

    while queue:
        cur, min_dist = queue.popleft()
        
        graph[i][cur] = min_dist
        graph[cur][i] = min_dist

        for neighbor, weight in tree[cur]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append((neighbor, min(min_dist, weight)))

for i in range(1, n+1):
    graph[i][i] = 0

for _ in range(q):
    k, v = map(int, input().split())
    answer = 0
    for i in range(1, n+1):
        if graph[v][i] >= k:
            answer += 1
    print(answer)
