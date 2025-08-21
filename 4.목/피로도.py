answer = []

def dfs(cur, num, graph, visited):
    nxt = []
    
    for i in range(len(graph)):
        if cur >= graph[i][0] and visited[i] == 0:
            visited[i] = 1
            dfs(cur - graph[i][1], num + 1, graph, visited)
            visited[i] = 0
            nxt.append(i)
    
    if not nxt:
        answer.append(num)
        return

def solution(k, dungeons):
    visited = [0] * (len(dungeons)) # 던전 수 만큼 visited
    
    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1
            dfs(k-dungeons[i][1], 1, dungeons, visited)
            visited[i] = 0
    
    
    return max(answer)
