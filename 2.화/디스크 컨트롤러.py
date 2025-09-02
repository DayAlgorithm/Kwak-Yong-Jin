import heapq
from collections import deque

def solution(jobs):
    graph = []
    for i in range(len(jobs)):
        graph.append(jobs[i] + [i])
    
    graph = sorted(graph, key=lambda x : x[0])
    graph = deque(graph)
    print(graph)

    en_time = 0
    heap = []
    result = [0] * (len(graph)) # 걸린 시간 표시
    cnt = 0 # 현재 시각
    
    while graph or heap:
        while graph and graph[0][0] <= cnt:
            s, l, i = graph.popleft()
            heapq.heappush(heap, (l, s, i))
        
        if cnt >= en_time: # 작업이 끝났을 때
            if heap: # 레디 큐에 작업이 남아 있으면
                l, s, i = heapq.heappop(heap)
                en_time = cnt + l
                result[i] = en_time - s
        cnt += 1

    answer = sum(result) // len(result)
    return answer
