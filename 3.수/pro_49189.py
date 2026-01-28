from collections import deque

def bfs(s, visited, graph):
    queue = deque()
    queue.append(s)
    visited[s] = 0
    
    while queue:
        cur = queue.popleft()
        
        for nxt in graph[cur]:
            if visited[nxt] == -1:
                visited[nxt] = visited[cur] + 1
                queue.append(nxt)
    

def solution(n, edge):
    visited = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    for i in range(len(edge)):
        a, b = edge[i]
        graph[a].append(b)
        graph[b].append(a)
    
    bfs(1, visited, graph)
    _max = max(visited)
    answer = visited.count(_max)
    return answer
