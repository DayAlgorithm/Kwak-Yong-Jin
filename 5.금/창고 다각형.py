import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
graph.sort() # graph 좌표별 정렬
_max = max(graph, key=lambda x : x[1])[1]
start = graph[0][1]
end = graph[-1][1]

prev_height = start
prev_coord = graph[0][0]
answer = 0
nxt = 0
for i in range(1, len(graph)):
    if prev_height > graph[i][1]: # 이전 높이가 더 높으면 패스
        continue
    else:
        answer += (graph[i][0] - prev_coord) * prev_height
        prev_height = graph[i][1]
        prev_coord = graph[i][0]
        
    if prev_height == _max:
        nxt = i
        break

prev_height = end
prev_coord = graph[-1][0]
for i in range(len(graph)-1, nxt - 1, -1):
    if prev_height > graph[i][1]:
        continue
    else:
        answer += (prev_coord - graph[i][0]) * prev_height
        prev_height = graph[i][1]
        prev_coord = graph[i][0]

print(answer + _max)
