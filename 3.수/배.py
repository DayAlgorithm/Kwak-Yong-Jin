import sys
import bisect
input = sys.stdin.readline

n = int(input())
crains = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))
boxes.sort()
crains.sort()

if boxes[-1] > crains[-1]:
    print(-1)
    exit(0)

cnt = 0
box_cnt = 0
while box_cnt < m:
    for crain in crains:
        idx = bisect.bisect_right(boxes, crain)
        if idx > 0:
            boxes.pop(idx - 1)
            box_cnt += 1
    
    cnt += 1

print(cnt)
