from collections import deque
def solution(maps):
    n, m = len(maps), len(maps[0]) # len(maps)는 행의 개수, len(maps[0])은 행의 개수 (n, m이 1보다 크기 때문에)
    visited = [[-1] * m for _ in range(n)] 
    dy = [-1, 0, 1, 0] 
    dx = [0, 1, 0, -1]
    
    queue = deque()
    queue.append([0, 0]) 
    visited[0][0] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < len(maps) and 0 <= nx < len(maps[0]):
                if maps[ny][nx] == 1 and visited[ny][nx] == -1:
                    queue.append([ny, nx])
                    visited[ny][nx] = visited[y][x] + 1
                    
    return visited[n-1][m-1]
