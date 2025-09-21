import sys
input = sys.stdin.readline

def dfs(start):
    visited = [False] * (n+1)
    stack = [start]
    while stack:
        cur = stack.pop()
        if visited[cur]:
            continue
        visited[cur] = True
        nxt = graph[cur]
        if nxt == start:
            result.append(start)
            return
        if not visited[nxt]:
            stack.append(nxt)
    

n = int(input())
graph = [0] + [int(input()) for _ in range(n)]
result = []

for i in range(1, n+1):
    dfs(i)

print(len(result))
print(*result, sep='\n')
