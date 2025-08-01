import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')
 
w, h= map(int, input().split())
graph = [list(input().rstrip()) for _ in range(h)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[[INF] * 4 for _ in range(w)] for _ in range(h)]

C = []
for i in range(h):
    for j in range(w):
        if graph[i][j] == 'C':
            C.append((i, j))

sx, sy = C[0]
ex, ey = C[1]

queue = deque()
for d in range(4):
    visited[sx][sy][d] = 0
    queue.append((sx, sy, d))

while queue:
    x, y, d = queue.popleft()
    nx, ny = x + dx[d], y + dy[d]

    while 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '*':
        for nd in range(4):
            if d == nd:
                cost = 0
            else:
                cost = 1

            if visited[nx][ny][nd] > visited[x][y][d] + cost:
                visited[nx][ny][nd] = visited[x][y][d] + cost
                if cost == 0:
                    queue.appendleft((nx, ny, nd))
                else:
                    queue.append((nx, ny, nd))

        nx += dx[d]
        ny += dy[d]

print(min(visited[ex][ey]))
