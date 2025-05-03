import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(y, x):
    queue = deque()
    visited[y][x] = 1
    queue.append([y, x])
    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= m: continue
            if graph[ny][nx] == 0 or visited[ny][nx] >= 1: continue
            visited[ny][nx] += (visited[y][x] + 1)
            queue.append([ny, nx])
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)

for i in range(n): # 출력하는 부분만 좀 신경써서, 원래 못가는 부분은 0, 섬나라처럼 고립되어 있는 곳은 -1
    for j in range(m):
        if graph[i][j] == 0:
            print(0, end = ' ')
        elif graph[i][j] != 0:
            if visited[i][j] == 0:
                print(-1, end=' ')
            else:
                print(visited[i][j] - 1, end=' ')
    print()
