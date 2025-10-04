import sys
from collections import deque

n, T = map(int, sys.stdin.readline().split())
holes = set()
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    holes.add((x, y))

queue = deque([(0, 0, 0)])

visited = set([(0, 0)])

while queue:
    x, y, count = queue.popleft()
    if y == T:
        print(count)
        sys.exit()
    for dy in range(-2, 3):
        for dx in range(-2, 3):
            if dx == 0 and dy == 0:
                continue
                
            nx, ny = x + dx, y + dy
            if (nx, ny) in holes and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny, count + 1))    
print(-1)
