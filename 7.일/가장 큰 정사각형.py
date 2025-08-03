import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
d = [[0] * m for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, list(input().rstrip()))))

answer = 0
for i in range(n):
    for j in range(m):
        if i == 0 or j == 0:
            d[i][j] = graph[i][j]
        elif graph[i][j] == 0:
            d[i][j] = 0
        else:
            d[i][j] = min(d[i - 1][j - 1], d[i - 1][j], d[i][j - 1]) + 1
        answer = max(d[i][j], answer)

print(answer * answer)
