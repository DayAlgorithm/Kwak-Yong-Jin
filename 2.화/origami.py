import sys
import math
input = sys.stdin.readline

def func(low, high, n):
    if low >= high:
        return

    mid = (low + high) // 2
    d[n].append(s[mid])

    func(low, mid, n + 1)
    func(mid + 1, high, n + 1)

t = int(input())
for _ in range(t):
    s = list(input().strip())
    n = int(math.log(len(s) + 1, 2))
    d = [[] for _ in range(n)]

    func(0, len(s), 0)
    
    flag = True
    for i in range(len(d)):
        prev = d[i][0]
        for j in range(1, len(d[i])):
            if prev == d[i][j]:
                flag = False
                break
            prev = d[i][j]
        
        if flag == False:
            break
    
    if flag == False:
        print("NO")
    else:
        print("YES")
