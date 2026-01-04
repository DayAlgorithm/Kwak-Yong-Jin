import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cloud = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
for i in range(m): # 구름이 이미 생긴 이후 이동하는 것 관련
    d, s = map(int, input().split())
    nx = dx[d] * s # 이 만큼 이동해라
    ny = dy[d] * s

    chk = set() # 이미 구름이었던 곳 체킹용
    for j in range(len(cloud)): # 구름 이동하고 비내리기
        x, y = cloud[j]
        x = (x + nx)%n
        y = (y + ny)%n
        chk.add((x, y))
        cloud[j] = [x, y]
        graph[x][y] += 1
    
    # 물복사버그
    for j in range(len(cloud)):
        x, y = cloud[j]
        cnt = 0
        if (0 <= x - 1 < n) and (0 <= y - 1 < n):
            if graph[x-1][y-1] >= 1:
                cnt += 1
        
        if (0 <= x - 1 < n) and (0 <= y + 1 < n):
            if graph[x-1][y+1] >= 1:
                cnt += 1
        
        if (0 <= x + 1 < n) and (0 <= y - 1 < n):
            if graph[x+1][y-1] >= 1:
                cnt += 1
        
        if (0 <= x + 1 < n) and (0 <= y + 1 < n):
            if graph[x+1][y+1] >= 1:
                cnt += 1
        
        graph[x][y] += cnt
    
    # 새로운 구름 만들기
    cloud = []
    for j in range(n):
        for k in range(n):
            if (j, k) not in chk:
                if graph[j][k] >= 2:
                    graph[j][k] -= 2
                    cloud.append([j, k])

answer = 0
for i in range(n):
    answer += sum(graph[i])
print(answer)
