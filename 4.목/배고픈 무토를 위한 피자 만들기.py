import sys
input = sys.stdin.readline

n = int(input())
r, c = map(int, input().split())
pizza = [[False] * (n + 1) for _ in range(n + 1)]
ans = []

for i in range(1, n + 1):
    row = [0] + list(input().rstrip())
    for j in range(1, n + 1):
        if row[j] == '#':
            pizza[i][j] = True

for i in range(1, c):
    ans.append(f"L {r} push")
for i in range(n, c, -1):
    ans.append(f"R {r} push")
for i in range(1, r):
    ans.append(f"U 1 push")
for i in range(n, r, -1):
    ans.append(f"D 1 push")

for i in range(r - 1, 0, -1):
    for j in range(2, n + 1):
        ans.append(f"R {i} push")
    for j in range(2, n + 1):
        if not pizza[i][j]:
            ans.append(f"U {j} pull")

for i in range(r, n + 1):
    for j in range(2, n + 1):
        if i == r:
            break
        ans.append(f"R {i} push")
    for j in range(2, n + 1):
        if not pizza[i][j]:
            ans.append(f"D {j} pull")

for i in range(1, n + 1):
    if not pizza[i][1]:
        ans.append(f"L {i} pull")

print(len(ans))
for a in ans:
    print(a)           
