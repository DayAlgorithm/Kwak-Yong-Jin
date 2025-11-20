import sys
from collections import deque
input = sys.stdin.readline

def bfs(group):
    queue = deque()
    visited = set()
    queue.append(group[0])
    visited.add(group[0])

    while queue:
        cur = queue.popleft()

        for nxt in graph[cur]:
            if nxt in group and not nxt in visited:
                queue.append(nxt)
                visited.add(nxt)
    
    if len(visited) == len(group):
        return True
    
    
def dfs(tmp1, tmp2, cnt):
    if cnt == n+1:
        if not tmp1:
            return
        if not tmp2:
            return
        
        if bfs(tmp1) and bfs(tmp2):
            p1 = 0
            for i in range(len(tmp1)):
                p1 += persons[tmp1[i]]
            
            p2 = 0
            for i in range(len(tmp2)):
                p2 += persons[tmp2[i]]

            answer.append(abs(p1 - p2))
        return

    tmp1.append(cnt)
    dfs(tmp1, tmp2, cnt+1)
    tmp1.pop()

    tmp2.append(cnt)
    dfs(tmp1, tmp2, cnt+1)
    tmp2.pop()
    

n = int(input())
persons = [0] + list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(n):
    lst = list(map(int, input().split()))
    for num in lst[1:]:
        graph[i+1].append(num)

tmp1 = []
tmp2 = []
answer = []
dfs(tmp1, tmp2, 1)

if not answer:
    print(-1)
else:
    print(min(answer))
