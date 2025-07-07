import sys
import heapq
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    print(n//2 + 1)

    graph = [0] * n
    for i in range(int(n//10) + 1):
        lst = list(map(int, input().split()))
        for j in range(len(lst)):
            graph[i*10 + j] = lst[j]

    graph = deque(graph)
    heap = []
    cnt = 0
    print_cnt = 1
    print_cnt2 = 0
    while True:
        heapq.heappush(heap, graph.popleft())
        cnt += 1
        if cnt%2 == 1:
            if print_cnt2//10 == 1:
                print()
                print_cnt2 = 0
            
            pre_heap = []
            for i in range(print_cnt - 1):
                pre_heap.append(heapq.heappop(heap))

            tmp = heapq.heappop(heap)
            print(tmp, end=' ')

            while pre_heap:
                heapq.heappush(heap, pre_heap.pop())
                
            heapq.heappush(heap, tmp)
            print_cnt += 1
            print_cnt2 += 1
        if len(graph) == 0:
            break
    
    print()중앙값 구하기
