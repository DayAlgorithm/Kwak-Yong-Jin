import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))

d1 = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if graph[i] > graph[j]:
            d1[i] = max(d1[i], d1[j]+1)

d2 = [1 for _ in range(n)]
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if graph[i] > graph[j]:
            d2[i] = max(d2[i], d2[j]+1)

result = [0 for i in range(n)]
for i in range(n):
    result[i] = d1[i] + d2[i] -1 

print(max(result))
