import sys
input = sys.stdin.readline

n = int(input().strip())
graph = [0] + list(map(int, input().split()))
d = [[0]*(n+1) for _ in range(2)]

for i in range(1, n+1):
    if graph[i] >= 0:
        d[1][i] = max(d[1][i-1] + graph[i], graph[i])
        d[0][i] = max(d[0][i-1] + graph[i], graph[i])
    
    else:
        d[1][i] = max(d[0][i-1], d[1][i-1] + graph[i])
        d[0][i] = d[0][i-1] + graph[i]

result = 0
for i in range(2):
    result = max(result, max(d[i]))

flag = False
for i in range(1, n+1):
    if graph[i] >= 0:
        flag = True    # 모두 음수일 경우에는 아무것도 선택 안하니까 하나라도 선택하기 위한 flag
        break

if flag:
    print(result)
else:
    print(max(graph[1:]))
