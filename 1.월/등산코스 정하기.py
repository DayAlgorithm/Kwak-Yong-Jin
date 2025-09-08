import heapq

INF = float('inf')

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n+1)]
    for a, b, w in paths:
        graph[a].append((b, w))
        graph[b].append((a, w))
    
    intensity = [INF] * (n+1)
    pq = []
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(pq, (0, gate))
    
    summits_set = set(summits)
    
    while pq:
        cur_intensity, cur = heapq.heappop(pq)
        
        if intensity[cur] < cur_intensity:
            continue
        if cur in summits_set: 
            continue
        
        for nxt, w in graph[cur]:
            next_intensity = max(cur_intensity, w)
            if intensity[nxt] > next_intensity:
                intensity[nxt] = next_intensity
                heapq.heappush(pq, (next_intensity, nxt))
    
    summits.sort()
    answer = [0, INF]
    for summit in summits:
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
    
    return answer
