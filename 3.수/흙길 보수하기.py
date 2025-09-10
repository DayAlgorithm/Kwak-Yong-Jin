import sys
input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
graph.sort()

cnt = 0
now = 0  

for s, e in graph:
    if now < s:
        now = s
    if now >= e:
        continue
    length = e - now
    need = (length + L - 1) // L 
    cnt += need
    now += need * L

print(cnt)
