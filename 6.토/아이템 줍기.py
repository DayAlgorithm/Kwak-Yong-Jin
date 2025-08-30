from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 좌표 2배 확장
    graph = [[0] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = -1  # 내부
                elif graph[i][j] != -1: 
                    graph[i][j] = 1   # 테두리

    # BFS
    dx, dy = [-1,0,1,0], [0,1,0,-1]
    q = deque()
    q.append((characterX*2, characterY*2))
    visited = [[-1]*102 for _ in range(102)]
    visited[characterX*2][characterY*2] = 0
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < 102 and 0 <= ny < 102:
                if visited[nx][ny] == -1 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))
    
    return visited[itemX*2][itemY*2] // 2
