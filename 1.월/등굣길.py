from collections import deque
def solution(m, n, puddles):
    dp = [[0] * m for _ in range(n)]
    graph = [[0] * m for _ in range(n)]
    for x, y in puddles:
        graph[y-1][x-1] = 1
    
    dy = [1, 0]
    dx = [0, 1]
    dp[0][0] = 1

    queue = deque([[0, 0]])
    while queue:
        y, x = queue.popleft()

        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 > ny or ny >= n or 0 > nx or nx >= m:
                continue
            if graph[ny][nx] == 1:
                continue
            if dp[ny][nx] == 0: # 만약 한 번도 지나친 적 없는 길이면 그냥 이전 경우의 수 복사
                dp[ny][nx] = dp[y][x]
                queue.append([ny, nx])
            else:
                dp[ny][nx] = (dp[ny][nx] + dp[y][x])%1000000007 # 한 번 지나간적 있는 길이면 이전 경우의 수 더해주고 queue에는 넣지 않음
            
    answer = dp[n-1][m-1]
    return answer
