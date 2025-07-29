import sys
from collections import deque
input = sys.stdin.readline

def rotation(x, di): # 현재 톱니 상태랑 방향 받음
    x = deque(list(x))
    if di == 1: # 시계 방향이면 마지막 톱니가 맨 앞으로
        tmp = x.pop()
        x.appendleft(tmp)
    
    else: # 반시계 방향이면 처음 톱니가 맨 뒤로
        tmp = x.popleft()
        x.append(tmp)
    
    x = list(x)
    return "".join(x)

t1 = input().rstrip()
t2 = input().rstrip()
t3 = input().rstrip()
t4 = input().rstrip()

k = int(input())
for _ in range(k):
    cur, mov = map(int, input().split())
    # 회전 시키기 전에 어떤 톱니바퀴를 어떻게 회전시킬지 미리 파악
    result = []
    if cur == 1:
        result.append([t1, mov, 1])
        if t1[2] != t2[6]: # 극이 다르면
            if mov == 1:
                result.append([t2, -1, 2])
                mov2 = -1
            else:
                result.append([t2, 1, 2])
                mov2 = 1

            if t2[2] != t3[6]:
                if mov2 == 1:
                    result.append([t3, -1, 3])
                    mov3 = -1
                else:
                    result.append([t3, 1, 3])
                    mov3 = 1

                if t3[2] != t4[6]:
                    if mov3 == 1:
                        result.append([t4, -1, 4])
                    else:
                        result.append([t4, 1, 4])
    elif cur == 2:
        result.append([t2, mov, 2])
        if t1[2] != t2[6]:
            if mov == 1:
                result.append([t1, -1, 1])
            else:
                result.append([t1, 1, 1])
            
        if t2[2] != t3[6]:
            if mov == 1:
                result.append([t3, -1, 3])
                mov2 = -1
            else:
                result.append([t3, 1, 3])
                mov2 = 1

            if t3[2] != t4[6]:
                if mov2 == 1:
                    result.append([t4, -1, 4])
                else:
                    result.append([t4, 1, 4])

    elif cur == 3:
        result.append([t3, mov, 3])
        if t2[2] != t3[6]:
            if mov == 1:
                result.append([t2, -1, 2])
                mov2 = -1
            else:
                result.append([t2, 1, 2])
                mov2 = 1
        
            if t2[6] != t1[2]:
                if mov2 == 1:
                    result.append([t1, -1, 1])
                else:
                    result.append([t1, 1, 1])
                
        if t3[2] != t4[6]:
            if mov == 1:
                result.append([t4, -1, 4])
            else:
                result.append([t4, 1, 4])
    
    elif cur == 4:
        result.append([t4, mov, 4])
        if t4[6] != t3[2]:
            if mov == 1:
                result.append([t3, -1, 3])
                mov2 = -1
            else:
                result.append([t3, 1, 3])
                mov2 = 1
            
            if t3[6] != t2[2]:
                if mov2 == 1:
                    result.append([t2, -1, 2])
                    mov3 = -1
                else:
                    result.append([t2, 1, 2])
                    mov3 = 1
            
                if t2[6] != t1[2]:
                    if mov3 == 1:
                        result.append([t1, -1, 1])
                    else:
                        result.append([t1, 1, 1])
    
    for i in range(len(result)):
        tmp = rotation(result[i][0], result[i][1])
        idx = result[i][2]

        if idx == 1:
            t1 = tmp
        elif idx == 2:
            t2 = tmp
        elif idx == 3:
            t3 = tmp
        else:
            t4 = tmp
            
answer = 0
if t1[0] == '1':
    answer += 1

if t2[0] == '1':
    answer += 2

if t3[0] == '1':
    answer += 4

if t4[0] == '1':
    answer += 8

print(answer)
