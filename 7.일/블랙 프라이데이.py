import sys
import bisect
input = sys.stdin.readline

N, C = map(int, input().split())
graph = list(map(int, input().split()))
graph.sort()

# 1. 하나만 선택
for w in graph:
    if w == C:
        print(1)
        sys.exit()

# 2. 두 개 선택 (투 포인터)
left, right = 0, N - 1
while left < right:
    s = graph[left] + graph[right]
    if s == C:
        print(1)
        sys.exit()
    if s < C:
        left += 1
    else:
        right -= 1

# 3. 세 개 선택 (이중 루프 + 이분 탐색)
for i in range(N):
    for j in range(i + 1, N):
        target = C - graph[i] - graph[j]
        if target <= 0:
            continue
        # 이분탐색으로 target이 존재하는지 확인
        idx = bisect.bisect_left(graph, target)
        # idx가 i나 j와 다르고, 범위 안이고, 값이 target과 같으면 OK
        if idx < N and graph[idx] == target and idx != i and idx != j:
            print(1)
            sys.exit()

# 불가능할 경우
print(0)
