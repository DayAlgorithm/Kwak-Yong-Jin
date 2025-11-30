import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
codes = ['']
code_idx = {}
for i in range(1, n + 1):
    code = input().strip()
    codes.append(code)
    code_idx[code] = i
        
s, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    cur = list(codes[i])
    
    for j in range(k):
        pre = cur[j]
    
        if pre == '0':
            cur[j] = '1'
        else:
            cur[j] = '0'
        
        nxt = "".join(cur)
        
        if nxt in code_idx:
            target_idx = code_idx[nxt]
            if target_idx != i:
                graph[i].append(target_idx)
        
        cur[j] = pre

queue = deque([s])
visited = [-1] * (n + 1)
visited[s] = 0

while queue:
    cur = queue.popleft()
    
    if cur == e:
        break
    
    for nxt in graph[cur]:
        if visited[nxt] == -1:
            visited[nxt] = cur
            queue.append(nxt)

if visited[e] == -1:
    print(-1)
else:
    path = []
    curr = e
    while curr != 0:
        path.append(curr)
        curr = visited[curr]
    print(*(path[::-1]))
