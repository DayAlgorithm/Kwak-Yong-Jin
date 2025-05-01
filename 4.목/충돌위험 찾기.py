from collections import Counter # 개수를 세는 모듈

def solution(points, routes):
    robots = []
    for route in routes:
        path = []
        step = 0
        x, y = points[route[0]-1]
        path.append((x, y, step))
        for i in range(1, len(route)):
            sx, sy = points[route[i-1]-1]
            ex, ey = points[route[i]-1]
            while sx != ex or sy != ey: # sx먼저 움직이고 그 다음에 sy 움직이기
                if sx != ex:
                    sx += 1 if sx < ex else -1
                elif sy != ey:
                    sy += 1 if sy < ey else -1
                step += 1
                path.append((sx, sy, step))
        robots.append(path)
    
    counter = Counter() # 개수 세기
    for path in robots:
        for pos in path:
            counter[pos] += 1
    
    return sum(1 for v in counter.values() if v > 1) # 지나온 기록들 중 1 이상이면 충돌이기에 count하기
