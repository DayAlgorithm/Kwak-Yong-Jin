import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

l, r = 0, N-1
best = float('inf')
ans = (0, 0)

while l < r:
    s = arr[l] + arr[r]

    if abs(s) < best:
        best = abs(s)
        ans = (arr[l], arr[r])

    if s < 0:  
        l += 1
    elif s > 0:
        r -= 1
    else:      
        break

print(ans[0], ans[1])
