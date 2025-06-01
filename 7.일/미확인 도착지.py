import sys
import heapq
input = sys.stdin.readline

def dijkstra(start, n, graph):
    dist = [float('inf')] * (n+1)
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        cost, cur = heapq.heappop(heap)
        if dist[cur] < cost:
            continue
        for nxt, w in graph[cur]:
            if dist[nxt] > dist[cur] + w:
                dist[nxt] = dist[cur] + w
                heapq.heappush(heap, (dist[nxt], nxt))
    return dist

T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))
    end_candi = [int(input()) for _ in range(t)]

    # 다익스트라를 여러 번 하는 이유
    # 최단 경로가 2개 이상 존재할 경우 s를 기준으로만 최단 경로를 구해버리면
    # 중복된 최단거리는 count가 안되기 때문에 틀린 답을 뱉을 수 있음
    ds = dijkstra(s, n, graph)
    dg = dijkstra(g, n, graph)
    dh = dijkstra(h, n, graph)

    result = []
    for dest in end_candi:
        gh_cost = None
        for nxt, w in graph[g]:
            if nxt == h:
                gh_cost = w
                break
        if gh_cost is None:
            continue

        # 만약 gh_cost를 지난 결과가 s를 기준으로 한 최단거리와 같으면 gh_cost를 지나는 거임
        # 그 전에 inf로 경로가 있는지부터 확인해야함 <- 이게 중요
        path1 = ds[g] + gh_cost + dh[dest]
        path2 = ds[h] + gh_cost + dg[dest]
        if min(path1, path2) == float('inf'):
            continue
        if ds[dest] == min(path1, path2):
            result.append(dest)

    result.sort()
    print(*result)
