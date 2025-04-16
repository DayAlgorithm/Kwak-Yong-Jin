import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    rot = 'N' # 현재 바라보는 방향
    tmp = [[0, 0], [0, 0]] # 0: X좌표의 (최소, 최대), 1: Y좌표의 (최소, 최대)
    cur = [0, 0] # 현재 위치
    graph = list(input().rstrip())

    for next in graph:
        if next == 'F':
            if rot == 'N':
                cur[1] += 1
                if tmp[1][1] < cur[1]:
                    tmp[1][1] = cur[1]

            elif rot == "S":
                cur[1] -= 1
                if tmp[1][0] > cur[1]:
                    tmp[1][0] = cur[1]
            
            elif rot == "W":
                cur[0] -= 1
                if tmp[0][0] > cur[0]:
                    tmp[0][0] = cur[0]

            elif rot == "E":
                cur[0] += 1
                if tmp[0][1] < cur[0]:
                    tmp[0][1] = cur[0]

        elif next == "B":
            if rot == "N":
                cur[1] -= 1
                if tmp[1][0] > cur[1]:
                    tmp[1][0] = cur[1]
            
            elif rot == "S":
                cur[1] += 1
                if tmp[1][1] < cur[1]:
                    tmp[1][1] = cur[1]

            elif rot == "W":
                cur[0] += 1
                if tmp[0][1] < cur[0]:
                    tmp[0][1] = cur[0]
            
            elif rot == "E":
                cur[0] -= 1
                if tmp[0][0] > cur[0]:
                    tmp[0][0] = cur[0]

        elif next == "L":
            if rot == "N":
                rot = "W"

            elif rot == "S":
                rot = "E"

            elif rot == "W":
                rot = "S"
            
            elif rot == "E":
                rot = "N"

        elif next == "R":
            if rot == "N":
                rot = "E"
            
            elif rot == "E":
                rot = "S"
            
            elif rot == "S":
                rot = "W"
            
            elif rot == "W":
                rot = "N"
 
    wide = abs(tmp[0][1] - tmp[0][0])  # 혹시 모를 절댓값 표시(아마 음수는 안나올거임)
    height = abs(tmp[1][1] - tmp[1][0])
    print(wide*height)
