import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))

i = n - 1
while i > 0 and graph[i-1] <= graph[i]:
    i -= 1

if i <= 0:
    print(-1)

else:
    j = n - 1
    while graph[j] >= graph[i-1]:
        j -= 1
    
    graph[i-1], graph[j] = graph[j], graph[i-1]

    answer = graph[:i] + sorted(graph[i:], reverse=True)
    print(*answer)
