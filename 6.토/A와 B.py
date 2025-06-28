import sys
input = sys.stdin.readline

s = list(input().rstrip())
t = list(input().rstrip())

while True:
    if len(s) == len(t):
        if s == t:
            print(1)
        else:
            print(0)
        
        break
    
    if t[-1] == 'A':
        t.pop()
    
    else:
        t.pop()
        t.reverse()
