import sys
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
stars = [tuple(map(int, input().split())) for _ in range(k)]

max_cnt = 0

for x1, _ in stars:
    for _, y1 in stars:
        cnt = 0

        if x1 + l > n:
            x1 = n - l
        
        if y1 + l > m:
            y1 = m - l

        for sx, sy in stars:
            if x1 <= sx <= x1 + l and y1 <= sy <= y1 + l:
                cnt += 1
        max_cnt = max(max_cnt, cnt)

print(k - max_cnt)
