import sys
from collections import deque
input = sys.stdin.readline

r,c,t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
cleaner = []
for i in range(r):
    if graph[i][0] == -1:
        cleaner.append(i)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for _ in range(t):
    # 미세먼지 확산
    temp = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if graph[i][j] >= 5:
                spread = graph[i][j] // 5
                for k in range(4):
                    ni, nj = i+dx[k], j+dy[k]
                    if 0<=ni<r and 0<=nj<c and graph[ni][nj] != -1:
                        temp[ni][nj] += spread
                        graph[i][j] -= spread
    
    for i in range(r):
        for j in range(c):
            graph[i][j] += temp[i][j]
    
    # 공기 청정기 작동
    # 상부 반시계방향
    up_row = cleaner[0]
    prev = 0
    for j in range(1, c):
        graph[up_row][j], prev = prev, graph[up_row][j]
    for i in range(up_row-1, -1, -1):
        graph[i][c-1], prev = prev, graph[i][c-1]
    for j in range(c-2, -1, -1):
        graph[0][j], prev = prev, graph[0][j]
    for i in range(1, up_row):
        graph[i][0], prev = prev, graph[i][0]
    
    # 하부 시계방향
    down_row = cleaner[1]
    prev = 0
    for j in range(1, c):
        graph[down_row][j], prev = prev, graph[down_row][j]
    for i in range(down_row+1, r):
        graph[i][c-1], prev = prev, graph[i][c-1]
    for j in range(c-2, -1, -1):
        graph[r-1][j], prev = prev, graph[r-1][j]
    for i in range(r-2, down_row, -1):
        graph[i][0], prev = prev, graph[i][0]

# 결과 계산
total = sum(sum(row) for row in graph) + 2  # 청정기(-1) 2개 보정
print(total)
