import sys
input = sys.stdin.readline

c, r = map(int, input().split())

graph = [[0 for _ in range(c)] for _ in range(r)]

dx = [-1, 0, 1, 0]  
dy = [0, 1, 0, -1] 

x, y = r - 1, 0 
dir = 0  
cnt = 1

while cnt <= c * r:
    graph[x][y] = cnt
    cnt += 1

    nx = x + dx[dir]
    ny = y + dy[dir]

    if not (0 <= nx < r and 0 <= ny < c) or graph[nx][ny] != 0:
        dir = (dir + 1) % 4
        nx = x + dx[dir]
        ny = y + dy[dir]

    x, y = nx, ny

n = int(input())
if n > r*c:
    print(0)
for i in range(len(graph)):
    for j in range(len(graph[i])):
        if graph[i][j] == n:
            print(j + 1, r - i)
