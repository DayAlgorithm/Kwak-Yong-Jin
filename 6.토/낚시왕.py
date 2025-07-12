import sys
input = sys.stdin.readline

N, M, m = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
sharks = []
for i in range(m):
    x, y, s, d, z = map(int, input().split())
    x -= 1
    y -= 1
    sharks.append([x, y, s, d, z])
    graph[x][y] = [s, d, z]

mov = [(), (-1, 0), (1, 0), (0, 1), (0, -1)]
cur = 0
answer = 0

for _ in range(M):
    # 낚시
    for i in range(N):
        if graph[i][cur]:
            answer += graph[i][cur][2]
            for idx, shark in enumerate(sharks):
                if shark[0] == i and shark[1] == cur:
                    sharks.pop(idx)
                    break
            graph[i][cur] = 0
            break

    cur += 1

    # 상어 이동
    new_graph = [[0 for _ in range(M)] for _ in range(N)]
    new_sharks = []

    for sx, sy, ss, sd, sz in sharks:
        # 속도 최적화
        if sd in [1,2]:
            ss %= (N-1)*2
        else:
            ss %= (M-1)*2

        x, y, d = sx, sy, sd
        for _ in range(ss):
            nx = x + mov[d][0]
            ny = y + mov[d][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                # 방향 반전
                if d == 1: d = 2
                elif d == 2: d = 1
                elif d == 3: d = 4
                elif d == 4: d = 3
                nx = x + mov[d][0]
                ny = y + mov[d][1]
            x, y = nx, ny

        # 같은 칸에 상어가 있으면 크기 비교
        if new_graph[x][y]:
            if new_graph[x][y][2] < sz:
                new_graph[x][y] = [ss, d, sz]
        else:
            new_graph[x][y] = [ss, d, sz]

    # new_sharks 갱신
    sharks = []
    for i in range(N):
        for j in range(M):
            if new_graph[i][j]:
                s, d, z = new_graph[i][j]
                sharks.append([i, j, s, d, z])
    graph = new_graph

print(answer)
