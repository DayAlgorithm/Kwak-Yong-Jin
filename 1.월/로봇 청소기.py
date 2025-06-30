import sys
input = sys.stdin.readline

n, m = map(int, input().split())
x, y, d = map(int, input().split())
rotation = [0, 1, 2, 3] # (d + 3)%4
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
clean = 1
graph[x][y] = -1

while True:
    flag = False
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if graph[nx][ny] == 0:
            flag = True
            break
    
    if flag:
        for _ in range(4):
            d = (d + 3)%4
            ny = y + dy[d]
            nx = x + dx[d]
            if graph[nx][ny] == 0:
                graph[nx][ny] = -1
                clean += 1
                y = ny
                x = nx
                break
    
    else:
        ny = y - dy[d]
        nx = x - dx[d]
        if graph[nx][ny] == 1:
            break
        else:
            y = ny
            x = nx

print(clean)
