import sys
input = sys.stdin.readline

s = input().rstrip()
n = len(s)
visited = [False] * n

def solve(l, r):
    if l > r:
        return
    
    idx = l
    for i in range(l+1, r+1):
        if s[i] < s[idx]:
            idx = i
    
    visited[idx] = True

    for i in range(n):
        if visited[i]:
            print("".join(s[i]), end='')
    
        else:
            print('', end='')
    print()

    solve(idx + 1, r)
    solve(l, idx - 1)

solve(0, n-1)
