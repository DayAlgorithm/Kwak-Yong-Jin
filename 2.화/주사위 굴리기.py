import sys
input = sys.stdin.readline

n, m, y, x, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
commands = list(map(int, input().split()))
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
dice = [0] * 7 # 1: top, 2: front, 3: right, 4: left, 5: back, 6: bottom
result = []

for command in commands:
    nx = x + dx[command - 1]
    ny = y + dy[command - 1]
    
    if 0 <= nx < m and 0 <= ny < n:
        # Determine new dice orientation based on command
        if command == 1:  # East
            dice[1], dice[3], dice[6], dice[4] = dice[4], dice[1], dice[3], dice[6]
        elif command == 2:  # West
            dice[1], dice[4], dice[6], dice[3] = dice[3], dice[1], dice[4], dice[6]
        elif command == 3:  # North
            dice[1], dice[2], dice[6], dice[5] = dice[5], dice[1], dice[2], dice[6]
        elif command == 4:  # South
            dice[1], dice[5], dice[6], dice[2] = dice[2], dice[1], dice[5], dice[6]
        
        # Update the map and dice values
        if graph[ny][nx] == 0:
            graph[ny][nx] = dice[6]
        else:
            dice[6] = graph[ny][nx]
            graph[ny][nx] = 0
        
        result.append(dice[1])
        x, y = nx, ny

print(*result, sep='\n')
