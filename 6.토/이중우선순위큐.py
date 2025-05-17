import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def solution(operations):
    answer = [0, 0]
    check = defaultdict(int) # 입력 받은 요소와 그 개수, 삭제하는 요소와 그 개수 다 저장
    minheap = []
    maxheap = []
    for order in operations:
        oper, num = order.split()
        num = int(num)

        if oper == "I":
            heapq.heappush(minheap, num)
            heapq.heappush(maxheap, -num)
            check[num] += 1
        else:
            if num == 1 and maxheap:
                while True:
                    tmp = -heapq.heappop(maxheap)
                    if check[tmp] >= 1:
                        check[tmp] -= 1
                        break
                    if not maxheap:
                        break
            elif num == -1 and minheap:
                while True: 
                    tmp = heapq.heappop(minheap)
                    if check[tmp] >= 1:
                        check[tmp] -= 1
                        break
                    if not minheap:
                        break
    if check:
        check = sorted(check.items())
        for i in range(len(check)):
            key, value = check[i]
            if value == 0:
                continue
            else:
                answer[1] = key
                break

        for i in range(len(check)-1, -1, -1):
            key, value = check[i]
            if value == 0:
                continue
            else:
                answer[0] = key
                break
    return answer

operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))
