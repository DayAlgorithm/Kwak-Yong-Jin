import sys
from collections import deque
input = sys.stdin.readline

def bfs(y, x, s):
    queue = deque()
    queue.append((y, x, s))

    while queue:
        y, x, s = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < n and 0 <= nx < m:
                # 벽인 경우
                if graph[ny][nx] == 1:
                    if s and visited[ny][nx][s] > visited[y][x][s] + 1:
                        visited[ny][nx][s] = visited[y][x][s] + 1
                        queue.append((ny, nx, s))

                # 검이 있는 칸
                elif graph[ny][nx] == 2:
                    ns = 1
                    if visited[ny][nx][ns] > visited[y][x][s] + 1:
                        visited[ny][nx][ns] = visited[y][x][s] + 1
                        queue.append((ny, nx, ns))

                # 빈 공간
                elif graph[ny][nx] == 0:
                    if visited[ny][nx][s] > visited[y][x][s] + 1:
                        visited[ny][nx][s] = visited[y][x][s] + 1
                        queue.append((ny, nx, s))


n, m, t = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
sword = []
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(m):
        graph[i][j] = lst[j]

        if lst[j] == 2:
            sword.append((i, j))

s = 0
INF = t+1
visited = [[[INF]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 0
if graph[0][0] == 2:
    visited[0][0][1] = 0
    s = 1

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
bfs(0, 0, s)
answer = min(visited[n-1][m-1])
if answer > t:
    print("Fail")
else:
    print(answer)
