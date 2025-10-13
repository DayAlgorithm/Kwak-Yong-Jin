def solution(park, routes):
    cur = [] 
    flag = True
    for i in range(len(park)): # 현재 위치 찾기 i가 세로, j가 가로
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                cur.append((i, j))
                flag = False
                break
        if not flag:
            break
            
    for i in range(len(routes)):
        x, y = cur.pop() # 현재 위치
        di, step = routes[i].split() # 방향, 거리
        step = int(step)
        n = len(park[0]) # 가로 길이
        m = len(park) # 세로 길이
        
        if di == 'N': # 세로 방향
            nx = x - step
            if nx >= 0: # 일단 안 벗어나면
                for j in range(x, nx - 1, -1):
                    if park[j][y] == 'X':
                        break
                else:
                    cur.append((nx, y))
                    
        elif di == 'S': # 세로 방향
            nx = x + step
            if nx <= m - 1:
                for j in range(x, nx+1):
                    if park[j][y] == 'X':
                        break
                else:
                    cur.append((nx, y))
            
        elif di == 'W':
            ny = y - step
            if ny >= 0:
                for j in range(y, ny - 1, -1):
                    if park[x][j] == 'X':
                        break
                else:
                    cur.append((x, ny))
                
        elif di == 'E':
            ny = y + step
            if ny <= n - 1:
                for j in range(y, ny + 1):
                    if park[x][j] == 'X':
                        break
                else:
                    cur.append((x, ny))
                    
        if not cur:
            cur.append((x, y))
            
    ex, ey = cur.pop()
    answer = [ex, ey]
    return answer
