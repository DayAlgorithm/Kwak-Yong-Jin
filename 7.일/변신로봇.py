import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def chg(cur, tmp):
    big = len(cur) if len(cur) > len(tmp) else len(tmp)
    total = 0
    for i in range(big):
        if i > len(cur):
            s = (int(tmp[i]))**2
        
        elif i > len(tmp):
            s = (int(cur[i]))**2

        else:
            s = (int(cur[i]) - int(tmp[i]))**2
        
        total += s
    
    return total

n = int(input())
mode = [input().rstrip() for _ in range(n)]
graph = [[] for _ in range(n)]

for i in range(n):
    cur = mode[i]
    for j in range(i, n):
        tmp = mode[j]

        cost = chg(cur, tmp)
        graph[i].append([j, cost])
        graph[j].append([i, cost])

a, b = map(int, input().split())
a, b = a - 1, b - 1
dist = [INF] * n
dist[a] = 0
heap = [[dist[a], a]]

while heap:
    cost, cur = heapq.heappop(heap)
    if cost > dist[cur]:
        continue

    for nxt, nxtcost in graph[cur]:
        if dist[nxt] > dist[cur] + nxtcost:
            dist[nxt] = dist[cur] + nxtcost
            heapq.heappush(heap, [dist[nxt], nxt])
print(dist[b])
