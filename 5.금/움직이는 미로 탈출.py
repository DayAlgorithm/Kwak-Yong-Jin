import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y, walls, visited):
    queue = deque()
    queue.append((x, y))
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()

            if x == 0 and y == 7:
                return True
            
            if (x, y) in walls:
                continue

            for i in range(9):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < 8 and 0 <= ny < 8 and not (nx, ny) in visited and not (nx, ny) in walls:
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        if walls:
            visited = set()
        nxt_walls = set()
        for x, y in walls:
            if x < 7:
                nxt_walls.add((x+1, y))
        walls = nxt_walls

graph = [[0 for _ in range(8)] for _ in range(8)]
walls = set()
for i in range(8):
    lst = input().rstrip()
    for j in range(8):
        graph[i][j] = lst[j]
        if lst[j] == '#':
            walls.add((i, j))

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1] # 멈춤, 위부터 8방향
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]
visited = set()
print(1 if bfs(7, 0, walls, visited) else 0)
