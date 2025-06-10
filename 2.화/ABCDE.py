import sys
input = sys.stdin.readline

def dfs(cur, cnt):
    if cnt == 5:
        print(1)
        sys.exit()
    
    if graph[cur]:
        for friend in graph[cur]: # 백백트래킹킹
            if visited[friend] != 1:
                visited[friend] = 1
                dfs(friend, cnt + 1)
                visited[friend] = 0

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [0] * (n)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n): # 그냥 백트래킹
    visited[i] = 1
    dfs(i, 1)
    visited[i] = 0

print(0)
