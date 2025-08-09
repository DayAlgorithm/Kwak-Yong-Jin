import sys
import heapq
input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []
for i in range(n):
    num = int(input())
    
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, (-num, num))
    else:
        heapq.heappush(right_heap, (num, num))

    if right_heap and left_heap[0][1] > right_heap[0][0]:
        _min = heapq.heappop(right_heap)[0]
        _max = heapq.heappop(left_heap)[1]
        heapq.heappush(left_heap, (-_min, _min))
        heapq.heappush(right_heap, (_max, _max))
    print(left_heap[0][1])    
