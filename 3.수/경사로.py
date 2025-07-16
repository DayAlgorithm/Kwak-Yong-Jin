import sys
input = sys.stdin.readline

N, L = map(int, input().split())
graph = [list(map(int , input().split())) for _ in range(N)]

answer = 0

# 행 체크
for i in range(N):
    used = [False] * N
    ok = True
    for j in range(N - 1):
        curr = graph[i][j]
        next = graph[i][j + 1]

        if curr == next:
            continue

        elif next - curr == 1:  # 오르막
            for k in range(j, j - L, -1):
                if k < 0 or graph[i][k] != curr or used[k]:
                    ok = False
                    break
                used[k] = True
            if not ok:
                break

        elif curr - next == 1:  # 내리막
            for k in range(j + 1, j + L + 1):
                if k >= N or graph[i][k] != next or used[k]:
                    ok = False
                    break
                used[k] = True
            if not ok:
                break

        else:  # 높이차가 2 이상이면 실패
            ok = False
            break
    if ok:
        answer += 1

# 열 체크
for j in range(N):
    used = [False] * N
    ok = True
    for i in range(N - 1):
        curr = graph[i][j]
        next = graph[i + 1][j]

        if curr == next:
            continue

        elif next - curr == 1:  # 오르막
            for k in range(i, i - L, -1):
                if k < 0 or graph[k][j] != curr or used[k]:
                    ok = False
                    break
                used[k] = True
            if not ok:
                break

        elif curr - next == 1:  # 내리막
            for k in range(i + 1, i + L + 1):
                if k >= N or graph[k][j] != next or used[k]:
                    ok = False
                    break
                used[k] = True
            if not ok:
                break

        else:  # 높이차가 2 이상이면 실패
            ok = False
            break
    if ok:
        answer += 1

print(answer)
