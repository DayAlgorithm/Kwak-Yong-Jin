import sys
import heapq
input = sys.stdin.readline

n = int(input())
chk = dict()
maxheap = []
minheap = []
for _ in range(n):
    p, l = map(int, input().split())
    chk[p] = l
    heapq.heappush(minheap, (l, p)) # 쉬운 문제
    heapq.heappush(maxheap, (-l, -p)) # 어려운 문제

m = int(input())
for _ in range(m):
    lst = list(input().rstrip().split())
    
    if lst[0] == 'add':
        chk[int(lst[1])] = int(lst[2]) # p문제와 l 레벨
        heapq.heappush(minheap, (int(lst[2]), int(lst[1])))
        heapq.heappush(maxheap, (-int(lst[2]), -int(lst[1])))
    elif lst[0] == 'solved':
        chk[int(lst[1])] = 0 # p문제를 해결하면 l 레벨은 0
    else:
        if lst[1] == '1': # 가장 어려운 문제
            while True:
                tmp = heapq.heappop(maxheap)
                if chk[-tmp[1]] == -tmp[0]:
                    print(-tmp[1])
                    heapq.heappush(maxheap, tmp) # 다시 넣어야지
                    break

        else:
            while True:
                tmp = heapq.heappop(minheap)
                if chk[tmp[1]] == tmp[0]:
                    print(tmp[1])
                    heapq.heappush(minheap, tmp) # 다시 넣어야지
                    break
