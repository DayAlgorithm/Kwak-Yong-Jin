import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 1 <= nx <= n and 1 <= ny <= m:
                if trash[nx][ny] == 1 and (nx, ny) not in visited:
                    cnt += 1
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    return cnt
n, m, k = map(int, input().split())
trash = [[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(k):
    a, b = map(int, input().split())
    trash[a][b] = 1

result = []
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
visited = set()

for i in range(1, n+1):
    for j in range(1, m+1):
        if trash[i][j] == 1:
            if (i, j) not in visited:
                visited.add((i, j))
                result.append(bfs(i, j))
print(max(result))
