import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[0 for _ in range(N+1)] for _ in range(N+1)]
indegree = [0] * (N + 1) # 위상정렬을 위한 차수 계산

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1 # 차수 입력

result = [0] * (N+1)
queue = deque()
for i in range(1, len(indegree)):
    if indegree[i] == 0:
        queue.append(i)
        result[i] = 1

while queue:
    cur = queue.popleft()

    if graph[cur]:
        for num in graph[cur]:
            indegree[num] -= 1

            if indegree[num] == 0:
                queue.append(num)
                result[num] = result[cur] + 1 # 다음 학기 기록

for i in range(1, len(result)):
    print(result[i], end=' ')
