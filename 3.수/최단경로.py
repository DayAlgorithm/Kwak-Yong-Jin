import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
INF = 1000000000
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)                     # 최단거리 측정하는 배열
check = defaultdict(int)

for i in range(e):
    src, des, cost = map(int, input().split())
    if check[src, des] == 0:
        check[src, des] = cost
    else:
        if check[src, des] > cost:
            check[src, des] = cost

for key, value in check.items():             # 정점 사에의 간선 중 가중치가 최소인 가중치만 기록하기
    src, des = key
    graph[src].append([des, value])

distance[k] = 0
heap = []
heapq.heappush(heap, [0, k])

while heap:
    cost, cur = heapq.heappop(heap)
    if distance[cur] < cost:                # 새롭게 업데이트 하려는 거리가 이미 더 짧은 경로로 기록되어 있으면 건너뛰기
        continue
    for des, c in graph[cur]:
        tmp = cost + c
        if tmp < distance[des]:
            distance[des] = tmp
            heapq.heappush(heap, [distance[des], des])
for num in distance[1:]:
    if num == INF:
        print('INF')
    else:
        print(num)
