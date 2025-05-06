import sys
from collections import deque, defaultdict # 딕셔너리 라이브러리
input = sys.stdin.readline

def moving(crazy, normal):
    n = len(crazy)
    for i in range(n):
        y, x = crazy.popleft()
        if abs(normal[0][0] - y) >= 1:
            y = y + 1 if y < normal[0][0] else y - 1
        if abs(normal[0][1] - x) >= 1:
            x = x + 1 if x < normal[0][1] else x - 1
        crazy.append([y, x])
        # 만약 I를 잡으면
        if y == normal[0][0] and x == normal[0][1]:
            return False
    return True
        
r, c = map(int, input().split())
dy = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dx = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
normal = deque()
crazy = deque()
graph = []

for i in range(r):
    s = input().rstrip()
    for j in range(len(s)):
        if s[j] == 'I':
            normal.append([i, j])
        elif s[j] == 'R':
            crazy.append([i, j])
    graph.append(list(s))
move = list(input().rstrip())
flag = True
cnt = 0
for num in move:
    if flag:
        num = int(num)
        cur_y, cur_x = normal.popleft()
        cur_y += dy[num]
        cur_x += dx[num]
        normal.append([cur_y, cur_x])
        flag = moving(crazy, normal)

        # 자기들끼리 부딪히는 경우
        position = defaultdict(int) # 딕셔너리 int형으로 라이브러리 하면, 없는 키 값 접근 시 자동으로 0으로 초기화 
        for pos in crazy:
            position[tuple(pos)] += 1
        crazy = deque(
            pos for pos in crazy
            if position[tuple(pos)] == 1
        )
        cnt += 1
    else:
        break

if flag:
    result = [['.'] * c for _ in range(r)]
    y, x = normal.popleft()
    result[y][x] = 'I'
    for i in range(len(crazy)):
        y, x = crazy.popleft()
        result[y][x] = 'R'
    for i in range(len(result)):
        print(''.join(result[i]))
else:
    print("kraj {}".format(cnt))
