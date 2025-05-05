import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque()
time = [0] * (n+1)
degrees = [0] * (n+1)
graph = [[] for _ in range(n+1)]
d = [0] * (n+1)

for i in range(1, n+1):
    lst = list(map(int, input().split()))
    time[i] = lst[0]
    degrees[i] = lst[1]
    if lst[1] == 0:
        queue.append(i)
        d[i] = time[i]
    for j in range(2, len(lst)):
        num = lst[j]
        graph[num].append(i)

while queue: # 위상정렬 + DP
    cur = queue.popleft()
    for nxt in graph[cur]:
        degrees[nxt] -= 1
        d[nxt] = max(d[nxt], d[cur] + time[nxt]) # 가장 오래걸리는 시간 기록
        if degrees[nxt] == 0:
            queue.append(nxt)

print(max(d[1:]))
