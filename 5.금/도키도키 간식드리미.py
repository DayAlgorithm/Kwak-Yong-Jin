import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque(list(map(int, input().split())))
_min = sorted(queue, reverse=True) # 다음에 나갈 친구 비교하는 값
queue2 = deque()


for i in range(n):
    tmp = queue.popleft()
    
    if tmp == _min[-1]:
        _min.pop()
        while queue2 and queue2[0] == _min[-1]: # 다음에 나갈 친구가 queue2의 앞에 있으면 나갈 수 있음
            queue2.popleft()
            _min.pop()
    
    else:
        queue2.appendleft(tmp)

queue2 = list(queue2)
ret = sorted(queue2)

if ret == queue2: # queue2에 남아 있는 요소들이 오름차순 정렬이면 다 나갈 수 있음
    print('Nice')
else:
    print('Sad')
