import sys
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
s = int(input())
tmp = 0

while s > 0 and tmp < n:
    max_index = graph.index(max(graph[tmp:tmp+s+1]))
    if max_index != tmp:
        graph[max_index], graph[max_index - 1] = graph[max_index - 1], graph[max_index]
        s -= 1
    else:
        tmp += 1
print(*graph)
