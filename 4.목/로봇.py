import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]
visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(m)] # 3차원 배열로 회전의 경우의 수까지 포함

src = list(map(lambda x: int(x) - 1, input().split()))
dst = list(map(lambda x: int(x) - 1, input().split())) # 1 -> 0 based BFS

q = deque([src + [0]]) # q에 x좌표, y좌표, d방향, c횟수
mov = [[0, 1], [0, -1], [1, 0], [-1, 0]]
step = [1, 2, 3] # 1칸 이동부터 3칸 이동까지
turn = [[2, 3], [0, 1]] # 회전 시 동쪽에서는 남, 북으로 회전 가능한데 이것이 2, 3임 <- 중요

while q:
    x, y, d, c = q.popleft()
    if visited[x][y][d]:
        continue
    if [x, y, d] == dst:
        print(c)
        break
    visited[x][y][d] = 1

    for nd in turn[d//2]: # 회전 <-  동, 서는 남, 북으로만 회전하므로 0,1 인경우는 2,3으로, 남, 북도 이와 같음
        q.append((x, y, nd, c + 1))

    for s in step:
        dx, dy = mov[d][0] * s, mov[d][1] * s
        if not (0 <= x + dx < m and 0 <= y + dy < n) or graph[x+dx][y+dy]: # 가는 경로 중간에 못 지가나는 부분이 있으면 break
            break
        q.append((x + dx, y + dy, d, c + 1))
