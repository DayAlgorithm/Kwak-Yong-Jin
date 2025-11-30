import sys
import heapq
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    a, b, c = map(int, input().split())
    graph.append((b, c, a))
graph.sort()
heap = []
answer = 0
for i in range(len(graph)):
    b, c, a = graph[i]

    if len(heap) == answer:
        if answer != 0 and heap[0] <= b:
            heapq.heappop(heap)
        else:
            answer += 1
        heapq.heappush(heap, c)
print(answer)
