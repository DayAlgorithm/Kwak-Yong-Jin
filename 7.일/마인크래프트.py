import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
min_height = min(map(min, land))
max_height = max(map(max, land))
best_time = float('inf')
best_height = 0

for target_height in range(min_height, max_height + 1):
    time = 0
    inventory = b

    for i in range(n):
        for j in range(m):
            current_height = land[i][j]
            if current_height > target_height:
                diff = current_height - target_height
                time += diff * 2
                inventory += diff
            elif current_height < target_height:
                diff = target_height - current_height
                time += diff
                inventory -= diff

    if inventory >= 0:
        if time < best_time or (time == best_time and target_height > best_height):
            best_time = time
            best_height = target_height
print(best_time, best_height)
