import sys
from itertools import combinations # 조합 사용하기
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
virus = []
cnt_zero = 0 # 0 개수 세기

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j] == 2:
            virus.append((i, j))
        elif row[j] == 0:
            cnt_zero += 1
    graph.append(row)

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
answer = []

for comb in combinations(virus, m):
    visited = [[-1]*n for _ in range(n)]
    queue = deque()
    for y, x in comb:
        queue.append((y, x))
        visited[y][x] = 0

    infected = 0
    max_day = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < n:
                if graph[ny][nx] != 1 and visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    queue.append((ny, nx))

                    if graph[ny][nx] == 0:
                        infected += 1
                        max_day = visited[ny][nx]

    if infected == cnt_zero:
        answer.append(max_day)

if answer:
    print(min(answer))
else:
    print(-1)
