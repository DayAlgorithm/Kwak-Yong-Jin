from collections import deque
def bfs(n, cur, visited, graph):
    queue = deque([cur])
    visited[cur] = 1
    while queue:
        x = queue.popleft()
        
        for i in range(n):
            if visited[i] == 0 and graph[x][i] == 1: # 현재 정점을 방문하지 않았고, 연결된 간선이 있다면
                visited[i] = 1
                queue.append(i)
        
def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            bfs(n, i, visited, computers)
            answer += 1 # bfs 돌아간 횟수 = 네트워크 수
    return answer
