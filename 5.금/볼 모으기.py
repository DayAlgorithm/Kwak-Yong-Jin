import sys
input = sys.stdin.readline

n = int(input())
s = list(input().rstrip())

def move_left(color): # 하나의 공을 왼쪽으로 전부 이동시키기
    cnt = 0
    flag = False
    for c in s:
        if c != color:
            flag = True
        if flag and c == color:
            cnt += 1
    return cnt

def move_right(color): # 하나의 공을 오른쪽으로 전부 이동시키기
    cnt = 0
    flag = False
    for c in reversed(s):
        if c != color:
            flag = True
        if flag and c == color:
            cnt += 1
    return cnt

ans = min(
    move_left('R'),  
    move_right('R'), 
    move_left('B'),  
    move_right('B') 
)
print(ans)
