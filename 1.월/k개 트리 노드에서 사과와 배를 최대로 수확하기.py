import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n-1):
    p, c = map(int, input().split())
    graph[p].append(c)
    graph[c].append(p) 

scores = list(map(int, input().split()))

visited = set()
q = deque()
init_mask = 1 << 0
q.append((init_mask, 1))
visited.add(init_mask)

max_product = -1
best_a, best_b = 0, 0

while q:                                  # BFS + 비트마스킹 하는 부분
    mask, cnt = q.popleft()
    apple, pear = 0, 0
    for i in range(n):
        if mask & (1 << i):
            if scores[i] == 1:
                apple += 1
            elif scores[i] == 2:
                pear += 1
    product = apple * pear
    if (product > max_product) or \
       (product == max_product and apple > best_a) or \
       (product == max_product and apple == best_a and pear > best_b):
        max_product = product
        best_a, best_b = apple, pear
   
    for i in range(n):                   
        if mask & (1 << i):
            for nxt in graph[i]:
                if not (mask & (1 << nxt)):
                    new_mask = mask | (1 << nxt)
                    if bin(new_mask).count('1') <= k and new_mask not in visited:
                        visited.add(new_mask)
                        q.append((new_mask, cnt+1))

print(best_a, best_b)
