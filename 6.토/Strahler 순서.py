import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k, m, p = map(int, input().split())
    indegree = [0] * (m+1)
    graph = [[] for _ in range(m+1)]
    for _ in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1 
    d = [0] * (m+1)
    history = [[] for _ in range(m+1)]

    queue = deque()
    for i in range(1, len(indegree)):
        if indegree[i] == 0:
            queue.append(i)
            d[i] = 1
    
    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            history[nxt].append(cur)
            if indegree[nxt] == 0:
                queue.append(nxt)

                tmp = []
                for past in history[nxt]:
                    tmp.append(d[past])
                
                tmp.sort(reverse=True)
                if len(tmp) > 1 and tmp[0] == tmp[1]:
                    d[nxt] = tmp[0] + 1
                
                else:
                    d[nxt] = tmp[0]
    
    print(k, d[m])
