import sys
from collections import deque
input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())
visited = [-1] * (F+1)
visited[S] = 0
queue = deque([S])

while queue:
    cur = queue.popleft()

    if cur == G:
        break
    
    # U인 경우
    if cur + U <= F:
        if visited[cur + U] == -1:
            queue.append(cur+U)
            visited[cur+U] = visited[cur] + 1
    
    if 0 < cur - D:
        if visited[cur - D] == -1:
            queue.append(cur - D)
            visited[cur - D] = visited[cur] + 1

if visited[G] == -1:
    print("use the stairs")
else:
    print(visited[G])
