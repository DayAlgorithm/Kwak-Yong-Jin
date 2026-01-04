import sys
import heapq
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
v = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
for i in range(len(p)):
    graph[p[i]].append(i+2)

candi = [(-v[0], 1)]
answer = 0
cnt = 0
while candi:
    cur_cost, cur = heapq.heappop(candi)
    answer += -cur_cost
    cnt += 1
    while graph[cur]:
        nxt = graph[cur].pop()
        heapq.heappush(candi, (-v[nxt-1], nxt))
        cnt += 1
    print(answer)
print(cnt)
