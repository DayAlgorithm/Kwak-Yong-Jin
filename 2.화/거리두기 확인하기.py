from collections import deque

def bfs(graph, y, x):
    visited = [[-1 for _ in range(5)] for _ in range(5)]
    queue = deque()
    queue.append((y, x))
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited[y][x] = 0
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < 5 and 0 <= nx < 5:
                if graph[ny][nx] == 'X':
                    continue
                    
                if visited[ny][nx] != -1:
                    continue
                    
                if graph[ny][nx] == 'O':
                    visited[ny][nx] = visited[y][x] + 1
                    if visited[ny][nx] >= 3:
                        continue
                    queue.append((ny, nx))
                    continue
                    
                if graph[ny][nx] == 'P':
                    visited[ny][nx] = visited[y][x] + 1
                    if visited[ny][nx] <= 2:
                        return 0
    return 1

def solution(places):
    answer = [] 

    for k in range(5):
        flag = 1
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == 'P':
                    flag = bfs(places[k], i, j)

                    if flag == 0:
                        break
            if flag == 0:
                break
        answer.append(flag)
    return answer
