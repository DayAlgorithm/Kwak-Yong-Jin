import sys
import heapq
input = sys.stdin.readline

n = int(input())
coords = []
for _ in range(n):
    h, o = map(int, input().split())
    if h < o:
        coords.append([h, o])
    else:
        coords.append([o, h])
d = int(input())

graph = []
for i in range(n):
    a, b = coords[i]
    if b - a <= d:
        graph.append([a, b])
graph = sorted(graph, key=lambda x : (x[1], x[0]))

answer = 0
heap = []

for s, e in graph:
    heapq.heappush(heap, s)

    while heap and heap[0] < e - d:
        heapq.heappop(heap)
    
    answer = max(answer, len(heap))
print(answer)
