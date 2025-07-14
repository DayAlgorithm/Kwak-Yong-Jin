import sys
import heapq
input = sys.stdin.readline

n = int(input())
lpg = [tuple(map(int, input().split())) for _ in range(n)]
l, p = map(int, input().split())

cnt = 0
lpg.sort()
heap = []
cur = 0

for i in range(n):
    if cur >= l:
        break
    a, b = lpg[i]
    p -= (a - cur)
    cur = a
    if p < 0:
        while True:
            gas = -heapq.heappop(heap)
            p += gas
            cnt += 1

            if p >= 0:
                break

            if not heap:
                print(-1)
                sys.exit()
    heapq.heappush(heap, -b)

p -= (l - cur)
if p < 0:
    while True:
        gas = -heapq.heappop(heap)
        p += gas
        cnt += 1

        if p >= 0:
            break

        if not heap:
            print(-1)
            sys.exit()
print(cnt)
