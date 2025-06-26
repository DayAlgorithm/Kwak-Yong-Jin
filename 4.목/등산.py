import sys
import heapq
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m, t, d = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    s = input().rstrip()
    for j in range(len(s)):
        if s[j].isupper():
            graph[i][j] = ord(s[j]) - 65
        else:
            graph[i][j] = ord(s[j]) - 71

dist1 = [[float('inf') for _ in range(m)] for _ in range(n)] # 가는 거
dist2 = [[float('inf') for _ in range(m)] for _ in range(n)] # 돌아오는 거
dist1[0][0] = 0 
dist2[0][0] = 0 
heap = [[dist1[0][0], [0, 0]]]

while heap:
    cost, coord = heapq.heappop(heap) 
    y, x = coord

    if cost > dist1[y][x]:
        continue

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < m:
            if abs(graph[ny][nx] - graph[y][x]) > t:  # 높이 차이가 t 이상이면 못감
                continue

            if graph[ny][nx] > graph[y][x]: # 오르막길
                nxtcost1 = (abs(graph[y][x] - graph[ny][nx]))**2
                nxtcost2 = 1 
            elif graph[ny][nx] == graph[y][x]: # 평지
                nxtcost1 = 1
                nxtcost2 = 1
            else: # 내리막길
                nxtcost1 = 1
                nxtcost2 = (abs(graph[y][x] - graph[ny][nx]))**2

            if dist1[y][x] + nxtcost1 <= d: # 가는 거 계산
                if dist1[ny][nx] > dist1[y][x] + nxtcost1:
                    dist1[ny][nx] = dist1[y][x] + nxtcost1
                    heapq.heappush(heap, [dist1[ny][nx], [ny, nx]])
            
            if dist2[y][x] + nxtcost2 <= d: # 돌아오는거 계산
                if dist2[ny][nx] > dist2[y][x] + nxtcost2:
                    dist2[ny][nx] = dist2[y][x] + nxtcost2

answer = -1
for i in range(n):
    for j in range(m):
        if dist1[i][j] == float('inf') or dist2[i][j] == float('inf'): # 못 가거나, 못 돌아오면 패스
            continue

        tmp = dist1[i][j] + dist2[i][j] # 갔다 오는 시간 계산
        if tmp > d: # 시간이 d보다 크면 cut
            continue

        answer = max(answer, graph[i][j]) # 결과

print(answer)
