import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
candi = []
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if graph[i][j] == 2:
            candi.append((i, j))
        
        if graph[i][j] == 1:
            graph[i][j] = '-'
    
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
result = []
for c in combinations(candi, m):
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    c = list(c)
    for i in range(len(c)):
        a, b = c[i]
        visited[a][b] = 0
    queue = deque(c)

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if graph[nx][ny] == '-':
                    continue

                if visited[nx][ny] != -1:
                    continue

                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
    
    _max = -1
    flag = True
    for i in range(n):
        for j in range(n):
            if graph[i][j] == '-':
                continue
            if visited[i][j] > _max:
                _max = visited[i][j]
            if visited[i][j] == -1:
                flag = False
                break
        if flag == False:
            break
    if flag:
        result.append(_max)

if not result:
    print(-1)
else:
    print(min(result))
