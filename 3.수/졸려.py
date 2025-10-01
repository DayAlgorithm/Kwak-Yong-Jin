import sys
from collections import deque
input = sys.stdin.readline

x = int(input())
s = list(map(str, input().rstrip()))
patterns = dict()
patterns["".join(s)] = 0
s = deque(s)
cnt = 0
while True:
    if cnt == x:
        break

    cnt += 1
    nxt = [0] * len(s)
    front = 0
    rear = len(s) - 1
    for i in range(len(s)):
        if i%2: # 홀수 이면
            nxt[rear] = s.popleft()
            rear -= 1
        else: # 짝수이면
            nxt[front] = s.popleft()
            front += 1

    nxt_tmp = "".join(nxt) 
    if nxt_tmp in patterns:
        break
    else:
        patterns[nxt_tmp] = cnt
        s = deque(nxt)

tmp = len(patterns) # 패턴 길이
x = x%tmp
for k, v in patterns.items():
    if v == x:
        print(k)
