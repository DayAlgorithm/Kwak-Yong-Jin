import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    total = 0
    while len(arr) > 1:
        a = heapq.heappop(arr)
        b = heapq.heappop(arr)
        cost = a + b
        total += cost
        heapq.heappush(arr, cost)
    print(total)
