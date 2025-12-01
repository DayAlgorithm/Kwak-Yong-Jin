import sys
from collections import deque
input = sys.stdin.readline

def bfs(cur):
    queue = deque()
    visited = [-1] * (n+1)
    queue.append(cur)
    visited[cur] = 0

    while queue:
        cur = queue.popleft()
        for nxt, cost in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + cost
                queue.append(nxt)
        
    _max = max(visited)
    return visited.index(_max), _max

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

u, _ = bfs(1)
v, answer = bfs(u)
print(answer)
