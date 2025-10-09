import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, adj):
    visited = [0] * (n + 1)
    q = deque([1])
    visited[1] = 1  # 1번 노드 거리 1로 시작

    while q:
        now = q.popleft()
        for nxt in adj[now]:
            if visited[nxt]:
                continue
            visited[nxt] = visited[now] + 1
            q.append(nxt)
    return visited


n = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 차량 정보 한 줄 입력
cars = list(map(int, input().split()))
car = [False] + [bool(c) for c in cars]  # 1-indexed

visited = bfs(n, adj)

# 차량이 있는 노드의 거리만 수집
arr = [visited[i] for i in range(1, n + 1) if car[i]]

# 내림차순 정렬
arr.sort(reverse=True)

# 각 차량의 (대기시간 + 이동시간) 최댓값 계산
max_time = 0
time = 0
for dist in arr:
    max_time = max(max_time, dist + time)
    time += 1

print(max_time)
