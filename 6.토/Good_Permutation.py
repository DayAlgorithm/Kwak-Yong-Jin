import sys
input = sys.stdin.readline

def chk(num):
    for i in range(1, len(num)//2+1):
        if num[-i:] == num[-(2*i):-i]:
            return False
    
    return True

def dfs(num, cur, end):
    if cur == end:
        print(num)
        sys.exit()

    for i in ['1', '2', '3']:
        nxt = num + i
        if chk(nxt):
            dfs(nxt, cur + 1, end)
    
n = int(input())
dfs('', 0, n)
