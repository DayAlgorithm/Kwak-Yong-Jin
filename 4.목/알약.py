import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

d = [[-1 for _ in range(31)] for _ in range(31)]

def func(w, h):
    if w == 0 and h == 0:
        return 1
    if w < 0 or h < 0:
        return 0
    if d[w][h] != -1:
        return d[w][h]

    d[w][h] = func(w - 1, h + 1) + func(w, h - 1)
    return d[w][h]

result = []
while True:
    n = int(input())
    if n == 0:
        break
    result.append(func(n, 0))
    d = [[-1 for _ in range(31)] for _ in range(31)]

for res in result:
    print(res)
