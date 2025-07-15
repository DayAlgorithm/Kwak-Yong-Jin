from collections import deque
from itertools import permutations
import sys
input = sys.stdin.readline

def bfs(sy, sx):
    dist = [[-1]*n for _ in range(m)]
    q = deque()
    q.append((sy, sx))
    dist[sy][sx] = 0
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny, nx = y + dy[d], x + dx[d]
            if 0 <= ny < m and 0 <= nx < n and graph[ny][nx] != 'x' and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                q.append((ny, nx))
    return dist

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = []
    pos = []
    for i in range(m):
        row = list(input().rstrip())
        graph.append(row)
        for j in range(n):
            if row[j] == 'o':
                pos.insert(0, (i, j))
            elif row[j] == '*':
                pos.append((i, j))

    L = len(pos)
    dist = [[-1]*L for _ in range(L)]
    flag = True
    for i in range(L):
        tmp = bfs(pos[i][0], pos[i][1])
        for j in range(L):
            dist[i][j] = tmp[pos[j][0]][pos[j][1]]
            if dist[i][j] == -1:
                flag = False

    if not flag:
        print(-1)
        continue

    ans = float('inf')
    for order in permutations(range(1, L)):
        total = 0
        now = 0
        for nxt in order:
            total += dist[now][nxt]
            now = nxt
        ans = min(ans, total)

    print(ans)
