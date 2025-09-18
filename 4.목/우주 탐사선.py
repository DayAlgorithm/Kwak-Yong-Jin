import sys
input = sys.stdin.readline

def dfs(x, cnt, length):
    if cnt == n:
        result.append(length)
        return
    
    for i in range(n):
        if visited[i] == 0:
            dfs_length = length + graph[x][i]

            visited[i] = 1
            dfs(i, cnt + 1, dfs_length)
            visited[i] = 0

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for l in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] > graph[i][l] + graph[l][j]:
                graph[i][j] = graph[i][l] + graph[l][j]

result = []
visited = [0] * n
visited[k] = 1
dfs(k, 1, 0)
print(min(result))
