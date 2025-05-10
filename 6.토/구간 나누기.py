import sys
input = sys.stdin.readline

n, m = map(int, input().split())
contain = [[0] + [-10e9] * m for _ in range(n+1)] # 현재 숫자를 포함하는 경우
noncontain = [[0] + [-10e9] * m for _ in range(n+1)] # 현재 숫자를 포함하지 않는 경우
for i in range(1, n+1):
    num = int(input()) # num은 현재 숫자
    for j in range(1, min(m, (i+1)//2) + 1):
        contain[i][j] = max(contain[i-1][j], noncontain[i-1][j-1])+num # 현재 숫자를 사용하는 경우
        noncontain[i][j] = max(contain[i-1][j], noncontain[i-1][j]) # 현재 숫자를 사용하지 않고 버리는 경우
print(max(contain[n][m], noncontain[n][m]))
