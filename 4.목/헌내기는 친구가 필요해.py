import sys
from collections import deque
input = sys.stdin.readline
def bfs(y, x):
    global answer
    queue = deque()
    queue.append((y,x))
    visited[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and visited[ny][nx] == 0:
                if graph[ny][nx] == 'X':
                    continue

                if graph[ny][nx] == 'P':
                    answer += 1
                    graph[ny][nx] = 'O'

                queue.append((ny,nx))
                visited[ny][nx] = 1
n,m=map(int, input().split())
graph=[list(input().rstrip()) for _ in range(n)]
cur_x, cur_y = 0, 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            cur_x, cur_y = i, j
visited = [[0 for _ in range(m)] for _ in range(n)]
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]
answer = 0
bfs(cur_x, cur_y)
print(answer if answer != 0 else 'TT')
