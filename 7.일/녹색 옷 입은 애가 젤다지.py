import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]
cnt = 0
while True:
    n = int(input())
    if n == 0:
        break
    cnt += 1
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)] # 방문 여부 체크
    dist = [[INF for _ in range(n)] for _ in range(n)] # 최단거리 저장
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]

    visited[0][0] = 1
    queue = deque()
    queue.append([0, 0])
    dist[0][0] = graph[0][0]

    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if visited[ny][nx] == 0:
                queue.append([ny, nx])
                dist[ny][nx] = graph[ny][nx] + dist[y][x]
                visited[ny][nx] = 1
            
            else:
                if dist[ny][nx] > dist[y][x] + graph[ny][nx]:
                    dist[ny][nx] = dist[y][x] + graph[ny][nx]
                    queue.append([ny, nx])
    print(f"Problem {cnt}: {dist[n-1][n-1]}")
