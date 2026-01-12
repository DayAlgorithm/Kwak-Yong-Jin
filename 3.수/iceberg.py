import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    visited.add((x, y))
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

years = 0
while True:
    visited = set()
    cnt = 0 # 빙산 수
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and (i, j) not in visited:
                bfs(i, j)
                cnt += 1
    
    if cnt >= 2:
        print(years)
        break
    
    years += 1
    multing = []
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                tmp = 0
                for k in range(4):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if 0 <= ni < n and 0 <= nj < m:
                        if graph[ni][nj] == 0:
                            tmp += 1
            
                multing.append((i, j, tmp))
    
    if not multing:
        print(0)
        break

    for i, j, mult in multing:
        graph[i][j] = max(0, graph[i][j] - mult)
