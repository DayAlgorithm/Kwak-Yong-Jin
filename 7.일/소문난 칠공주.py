from itertools import combinations
from collections import deque

graph = [list(input().strip()) for _ in range(5)]
answer = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

positions = [(i, j) for i in range(5) for j in range(5)]

def is_connected(group):
    visited = set()
    q = deque()
    q.append(group[0])
    visited.add(group[0])
    
    count = 1
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (ny, nx) in group and (ny, nx) not in visited:
                visited.add((ny, nx))
                q.append((ny, nx))
                count += 1
    return count == 7

for comb in combinations(positions, 7):
    s_count = sum(1 for y, x in comb if graph[y][x] == 'S')
    if s_count >= 4 and is_connected(comb):
        answer += 1

print(answer)
