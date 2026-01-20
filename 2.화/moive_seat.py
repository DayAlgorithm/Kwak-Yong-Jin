import sys
input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
vips = [int(input().rstrip()) for _ in range(m)]
d = [0] * (41)
d[0] = 1
d[1] = 1
d[2] = 2
for i in range(3, n+1):
    d[i] = d[i-2] + d[i-1]

sum = 1
if m >= 1:
    tmp = 0
    for i in range(m):
        sum *= d[vips[i]-1-tmp]
        tmp = vips[i]
    
    sum *= d[n-tmp]
else:
    sum = d[n]

print(sum)
