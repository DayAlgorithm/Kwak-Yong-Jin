import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(start_y, start_x, idx, node_pos, graph, n):
    visited = [[-1] * n for _ in range(n)]
    visited[start_y][start_x] = 0
    q = deque([(start_y, start_x)])
    result = []

    while q:
        y, x = q.popleft()

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < n and 0 <= nx < n:
                if visited[ny][nx] == -1 and graph[ny][nx] != '1':
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))

                    if (ny, nx) in node_pos:
                        target_idx = node_pos[(ny, nx)]
                        result.append((visited[ny][nx], idx, target_idx))
    return result

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x
        return True
    return False

n, m = map(int, input().split())
graph = [list(input().strip()) for _ in range(n)]

nodes = []
node_pos = dict()
idx = 0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'S' or graph[i][j] == 'K':
            nodes.append((i, j))
            node_pos[(i, j)] = idx
            idx += 1

edges = []
for i, (y, x) in enumerate(nodes):
    edges += bfs(y, x, i, node_pos, graph, n)

edges.sort()
parent = list(range(len(nodes)))
answer = 0
used = 0

for cost, a, b in edges:
    if union(a, b):
        answer += cost
        used += 1

if used == len(nodes) - 1:
    print(answer)
else:
    print(-1)
