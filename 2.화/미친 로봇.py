import sys
input = sys.stdin.readline

def dfs(loc, cnt, track, visited, n): # 백트래킹, cnt는 움직인 횟수
    global answer
    if cnt == n: # 움직인 횟수가 n번이 되려면, 모든 경로가 겹치지 않아야 함. 즉, 단순이동의 경로만 있음
        p = 1
        for m in track: # 확률 계산
            mp = prob_dic[m]
            p *= (mp*0.01)
        answer += p
        return
    y, x = loc
    for i in range(4):
        mv_y = y + move_y[i]
        mv_x = x + move_x[i]

        if visited[mv_y][mv_x] == 1: # 이미 방문했던 곳이면 방문 X
            continue
        
        loc[0] = mv_y
        loc[1] = mv_x 
        track.append(alpha_mv[i]) # 경로 추적을 위한 이동한 위치를 동, 서, 남, 북으로 저장
        visited[mv_y][mv_x] = 1
        dfs(loc, cnt+1, track, visited, n) # 백트래킹 구현 부분 
        visited[mv_y][mv_x] = 0
        track.pop()


prob = list(map(int, input().split()))
n = prob[0]
prob_dic = {'e':prob[1], 'w':prob[2], 's':prob[3], 'n':prob[4]} # 각 이동 경로마다의 확률
move_y = [1, -1, 0, 0]
move_x = [0, 0, 1, -1]
alpha_mv = ['e','w','s','n'] 
track = [] # 이동 경로 추적을 위한 배열
answer = 0 # 총 확률

visited = [[0]*(2*n+1) for _ in range(2*n+1)] # 한 방향으로 최대 n번 움직일 수 있기 때문에 2n+1
loc = [n, n] # 초기 시작을 visited 정중앙인 (n, n)에서 시작
visited[n][n] = 1
dfs(loc, 0, track, visited, n)
print(answer)
