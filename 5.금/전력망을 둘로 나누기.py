from collections import deque

def chk(cur, graph, visited, ban):
    queue = deque()
    queue.append(cur)
    
    while queue:
        x = queue.popleft()
        
        for nxt in graph[x]:
            if x == cur and nxt == ban:
                continue
                
            if nxt in visited:
                continue
                
            visited.add(nxt)
            queue.append(nxt)
            
def solution(n, wires):
    answer = -1
    result = []
    graph = [[] for _ in range(n+1)]
    for i in range(len(wires)):
        v1, v2 = wires[i]
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for i in range(len(wires)):
        v1, v2 = wires[i]
        
        # v1 기준 연결된 송전탑 수
        visited = set()
        visited.add(v1)
        chk(v1, graph, visited, v2)
        v1_cnt = len(visited)
        
        # v2 기준 연결된 송전탑 수
        visited = set()
        visited.add(v2)
        chk(v2, graph, visited, v1)
        v2_cnt = len(visited)
        
        result.append(abs(v1_cnt - v2_cnt))
    
    answer = min(result)
    return answer
