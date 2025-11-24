import sys
import heapq
input = sys.stdin.readline

n = int(input())
assignments = []
max_day = -1
for i in range(n):
    d, w = map(int, input().split())
    if d > max_day:
        max_day = d
    assignments.append((-w, d))

heapq.heapify(assignments)
result = 0
chk = [0] * (max_day + 1)
while assignments:
    score, last = heapq.heappop(assignments)
    tmp = 0
    flag = True
    for i in range(last, len(chk)):
        if chk[i] + 1 > i:
            flag = False
            break
    
    if flag:
        result += -score
        for i in range(last, len(chk)):
            chk[i] += 1
    
print(result)
