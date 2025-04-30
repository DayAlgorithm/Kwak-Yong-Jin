import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = [[0]*(m+1) for _ in range(n+1)]
graph = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    lst = list(map(int, input().split()))
    for j in range(1,m+1):
        graph[i][j] = lst[j]

for i in range(1, m+1):
    for j in range(n, -1, -1):
        for k in range(0, j+1):
            if d[j][0] < d[j-k][0] + graph[k][i]: # 일반적인 배낭문제와 같은 점화식
                d[j][0] = d[j-k][0] + graph[k][i]

                for t in range(1, m+1):  # 어느 기업에 투자했는지 알기 위한 반복문
                    if(t==i):
                        d[j][i] = k
                    else:
                        d[j][t] = d[j-k][t]
print(d[n][0])
for i in range(1, m+1):
    print(d[n][i], end=' ')
