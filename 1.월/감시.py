import sys
input = sys.stdin.readline

# 방향 정의: 상, 우, 하, 좌 (시계방향)
directions = [(-1,0), (0,1), (1,0), (0,-1)]

# CCTV 종류별 가능한 방향 조합
cctv_dirs = {
    1: [[0], [1], [2], [3]],                 # 1방향
    2: [[0,2], [1,3]],                       # 2방향 (반대 방향)
    3: [[0,1], [1,2], [2,3], [3,0]],        # 2방향 (직각 방향)
    4: [[0,1,2], [1,2,3], [2,3,0], [3,0,1]],# 3방향
    5: [[0,1,2,3]]                          # 4방향 모두
}

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

cctvs = []
answer = 1e9

# CCTV 위치 저장
for i in range(N):
    for j in range(M):
        if 1 <= graph[i][j] <= 5:
            cctvs.append((i,j,graph[i][j]))

def watch(area, y, x, dirs):
    for d in dirs:
        ny, nx = y, x
        while True:
            ny += directions[d][0]
            nx += directions[d][1]
            if not (0 <= ny < N and 0 <= nx < M):
                break
            if area[ny][nx] == 6:  # 벽 만나면 종료
                break
            if area[ny][nx] == 0:
                area[ny][nx] = '#'

def dfs(depth, area):
    global answer
    if depth == len(cctvs):
        count = 0
        for i in range(N):
            for j in range(M):
                if area[i][j] == 0:
                    count += 1
        answer = min(answer, count)
        return

    y, x, cctv_type = cctvs[depth]
    for dirs in cctv_dirs[cctv_type]:
        copied_area = [row[:] for row in area]
        watch(copied_area, y, x, dirs)
        dfs(depth + 1, copied_area)

dfs(0, graph)
print(answer)
