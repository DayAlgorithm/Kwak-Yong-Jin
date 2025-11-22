import sys
input = sys.stdin.readline

while True:
    line = input().strip()
    if not line:
        break

    x = int(line) * 10**7
    n = int(input())
    if n == 0:
        print('danger')
        continue
    l = [int(input()) for _ in range(n)]
    l.sort()
    start = 0
    end = n-1
    r1, r2 = 0, 0
    trig = -1
    while start < end:
        tmp = l[start] + l[end]

        if tmp == x:
            if abs(l[end]-l[start]) > trig:
                trig = abs(l[end]-l[start])
                r1 = l[start]
                r2 = l[end]
            start += 1
            end -= 1
        
        elif tmp > x:
            end -= 1
        
        else:
            start += 1

    if trig == -1:
        print('danger')
    else:
        print('yes', r1, r2)
