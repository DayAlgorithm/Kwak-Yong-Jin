import sys
input = sys.stdin.readline

n, l = map(int, input().split())
water = [list(map(int, input().split())) for _ in range(n)]
water.sort()

done = 0
cnt = 0
for i in range(len(water)):
    start, end = water[i]

    if done >= end:
        continue
    
    if start >= done:
        length = end - start
        
        if length%l == 0:
            cnt += length//l
            done = start + (length//l) * l
        
        else:
            cnt += (length//l + 1)
            done = start + (length//l + 1) * l
    
    else:
        length = end - done

        if length%l == 0:
            cnt += length//l
            done = done + (length//l) * l
        
        else:
            cnt += (length//l + 1)
            done = done + (length//l + 1) * l

print(cnt)
