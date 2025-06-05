import sys
from collections import deque
input = sys.stdin.readline

def bfs(s, e):
    queue = deque()
    queue.append(s)
    visited[s] = 1

    while queue:
        x = queue.popleft()

        for i in range(2):             # 정직하게 앞뒤로 갈 경우
            nx = x + dx[i]

            if nx <= 0 or nx > n:
                continue
            if visited[nx]:
                continue

            visited[nx] = visited[x] + 1
            if nx == e:
                return visited[nx] - 1

            queue.append(nx)
        
        if tel[x]:                      # 텔레포트 있는 경우
            for nx in tel[x]:
                if nx <= 0 or nx > n:
                    continue
                if visited[nx]:
                    continue
                visited[nx] = visited[x] + 1
                if nx == e:
                    return visited[nx] - 1 # 초깃값이 1이여서 1을 빼줌
                queue.append(nx)


n, m = map(int, input().split())
visited = [0] * (n+1)
s, e = map(int, input().split())
tel = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    tel[x].append(y)
    tel[y].append(x)
dx = [-1, 1]
print(bfs(s, e))
