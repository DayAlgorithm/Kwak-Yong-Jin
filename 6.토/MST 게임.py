import sys
import heapq
input = sys.stdin.readline

n,m,k = map(int, input().split())
edges = []
gra=[[] for _ in range(n+1)]

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(m):
    a,b = map(int, input().split())
    edges.append((i+1, a, b))
edges.sort()

for i in range(k):
    edges.sort()
    parent = [i for i in range(n+1)]
    cnt = 0
    ans = 0
    for cost, x, y in edges:
        if find(x) == find(y): continue
        cnt += 1
        ans += cost
        union(x, y)
    if cnt == n-1:
        print(ans, end=' ')
    else:
        print(0, end=' ')
    edges = edges[1:]
