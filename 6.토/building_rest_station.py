import sys
input = sys.stdin.readline

n, m, l = map(int, input().split())
if n != 0:
    graph = [0] + list(map(int, input().split())) + [l]
    graph.sort()
else:
    graph = [0, l]

low = 1
high = l

while low <= high:
    mid = (high + low) // 2

    total = 0
    for i in range(1, len(graph)):
        tmp = graph[i] - graph[i-1]
        total += (tmp - 1) // mid
    
    if total <= m:
        high = mid - 1
    
    else:
        low = mid + 1

print(low)
