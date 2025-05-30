import sys
import heapq
input = sys.stdin.readline

# union-find 이 부분으로 두 정점이 서로 연결되어 있는지 확인하고 연결되어 있지 않으면 연결한다
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a_root = find(a)
    b_root = find(b)
    if a_root != b_root:
        parent[b_root] = a_root

n = int(input())
parent = [i for i in range(n+1)]
heap = []
for i in range(1, n+1):
    a = list(map(int, input().split()))
    for j in range(i+1, n+1):
        heapq.heappush(heap, [a[j-1], i, j])

res = 0
cnt = len(heap)
for i in range(cnt):
    cost, src, des = heapq.heappop(heap)
    if find(src) != find(des):         # 두 부모가 같은지 확인 -> 즉 연결되어 있는지 확인
        union(src, des)
        res += cost

print(res)
