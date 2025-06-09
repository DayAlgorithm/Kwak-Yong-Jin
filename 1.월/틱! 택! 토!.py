import sys
input = sys.stdin.readline

start = int(input())
moves = [tuple(map(int, input().split())) for _ in range(9)]

board = [[0]*3 for _ in range(3)]
current = start
winner = 0

def check_win(player):
    for row in board:
        if all(cell == player for cell in row): # 가로검사
            return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)): # 세로검사
            return True

    if all(board[i][i] == player for i in range(3)): # 왼쪽 웨에서 오른쪽 아래로 대각선 검사
        return True
    
    if all(board[i][2-i] == player for i in range(3)): # 왼쪽 아래에서 오른쪽 위로 대각선 검사
        return True
    
    return False

for r, c in moves:
    row = r-1
    col = c-1
    board[row][col] = current
    
    if check_win(current):
        winner = current
        break
    
    current = 2 if current == 1 else 1

print(winner)
