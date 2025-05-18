import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

T = int(input())
for k in range(T):
    n, m = map(int, input().split())
    d = [INF] * m
    prev = [-1] * m
    graph = [[] for _ in range(m)]
    heap = [[0, 0,-1]]
    for i in range(n):
        a, b, c = map(int, input().split())
        graph[a].append([c, b]) # 비용 먼저, heap에서의 최소값 꺼내기
        graph[b].append([c, a])
        
    d[0] = 0
    while heap:
        cost, src, bf = heapq.heappop(heap)
        if cost > d[src]:
            continue
        prev[src] = bf # 경로 역추적을 위한 로직
        
        for nc, next in graph[src]:
            if d[src] + nc < d[next]:
                d[next] = d[src] + nc
                heapq.heappush(heap, [d[next], next, src])
    if d[m-1] == INF:
        print(f"Case #{k+1}: -1")
    else:
        st = m - 1
        result = [st]
        while True:
            if st == 0:
                break
            result.append(prev[st])
            st = prev[st]
        result.reverse()
        print(f"Case #{k+1}:", *result)
