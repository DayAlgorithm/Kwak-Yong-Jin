import sys
from collections import deque
input = sys.stdin.readline

def bfs(cur):
    queue = deque()
    queue.append(cur)
    visited = [0] * n
    visited[cur] = 1

    while queue:
        cur = queue.popleft()

        for i in range(len(graph[cur])):
            if graph[cur][i] == 1:
                if visited[i] == 0:
                    visited[i] = 1
                    queue.append(i)
                    neighbor.add(i+1)

n = int(input())
m = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
traversal = list(map(int, input().split()))

neighbor = set()
neighbor.add(traversal[0])
bfs(traversal[0] - 1)
traversal = set(traversal)
if traversal.issubset(neighbor):
    print('YES')
else:
    print('NO')
