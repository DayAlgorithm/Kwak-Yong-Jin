import sys
input = sys.stdin.readline

MOD = 100999
d = [[0] * 2001 for _ in range(2001)]

for i in range(2001):
    d[0][i] = 1       # 1~i 까지의 자연수의 합으로 0을 만드는 경우는 1 = 아에 선택 안하는 경우

for i in range(1, 2001):
    for j in range(1, 2001):
        d[i][j] = d[i][j-1]
        if i >= j:
            d[i][j] = (d[i][j] + d[i-j][j-1]) % MOD

t = int(input())
for _ in range(t):
    n = int(input())
    print(d[n][n])
