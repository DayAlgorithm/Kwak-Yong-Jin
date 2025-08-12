import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    minheap = []
    maxheap = []
    edict = defaultdict(int)
    for _ in range(k):
        order, num = input().rstrip().split()
        num = int(num)

        if order == 'I':
            edict[num] += 1 # 존재 개수 추가
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
        else: # order == 'D'
            if num == -1: # 최솟값 찾기
                flag = False
                while minheap:
                    tmp = heapq.heappop(minheap)
                    if edict[tmp] != 0: # 0이 아니면 존재하는 숫자니 빼버리고 끝
                        edict[tmp] -= 1
                        flag = True
                        break
                
                if flag == False: # 다 빼서 비었는데 최솟값이 없으면 넘기기
                    continue
            
            else: # 최댓값 찾기
                flag = False
                while maxheap:
                    tmp = -heapq.heappop(maxheap)
                    if edict[tmp] != 0:
                        edict[tmp] -= 1
                        flag = True
                        break
                
                if flag == False:
                    continue
    
    maxresult = []
    minresult = []
    cnt = 0
    for key, value in edict.items():
        if value != 0:
            for i in range(value):
                cnt += 1
                heapq.heappush(maxresult, -key)
                heapq.heappush(minresult, key)

    if cnt == 0:
        print("EMPTY")
    else:
        print(-maxresult[0], minresult[0])
