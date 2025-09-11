import sys
input = sys.stdin.readline

def chk(cur):
    global answer
    if cur == s:
        answer = 1
        return
    
    if len(cur) < len(s):
        return

    if cur[-1] == 'A':
        chk(cur[:-1])

    if cur[0] == 'B':
        chk(cur[1:][::-1])

    return 0
s = input().rstrip()
t = input().rstrip()
answer = 0
chk(t)
print(answer)
