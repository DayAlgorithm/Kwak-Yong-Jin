import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []

for num in list(map(int, input().split())): # 처음에 힙에 다 담기기
    heapq.heappush(heap, num)

for _ in range(n-1): # 힙의 크기를 n개로 계속해서 제한한
    for num in list(map(int, input().split())):
        if num > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap,num)
print(heap[0])
