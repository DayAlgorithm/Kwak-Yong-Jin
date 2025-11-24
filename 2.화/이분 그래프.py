import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (v+1) 
    flag = True   

    for i in range(1, v+1):
        if visited[i] == 0:
            queue = deque()
            queue.append(i)
            visited[i] = 1

            while queue:
                cur = queue.popleft()

                for nxt in graph[cur]:
                    if visited[nxt] == 0:
                        visited[nxt] = -visited[cur]
                        queue.append(nxt)
                    
                    elif visited[nxt] == visited[cur]:
                        flag = False
                        break
                
                if not flag:
                    break
        
        if not flag:
            break

    if flag:
        print("YES")
    else:
        print("NO")
