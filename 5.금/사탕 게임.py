import sys

input = sys.stdin.readline

n = int(input())
board = [list(input().strip()) for _ in range(n)]

ans = 0

def check():
    max_cnt = 1
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            if board[i][j] == board[i][j-1]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)

    for j in range(n):
        cnt = 1
        for i in range(1, n):
            if board[i][j] == board[i-1][j]:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 1
        max_cnt = max(max_cnt, cnt)
        
    return max_cnt

for i in range(n):
    for j in range(n):
        if j + 1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, check())
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]

        if i + 1 < n:
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, check())
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]

print(ans)
