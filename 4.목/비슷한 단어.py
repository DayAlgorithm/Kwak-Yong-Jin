import sys
input = sys.stdin.readline

n = int(input())
graph = [input().rstrip() for _ in range(n)]
sorting_graph = sorted(list(enumerate(graph)), key=lambda x:x[1]) # 초기 순서가 중요하기 때문에 인덱스랑 같이 저장하고, 문자열 기준으로 정렬

length = [0] * (n+1) # 각 문자열의 최대 접두사 길이 저장 배열
_max = 0 # 가장 긴 접두사의 길이

for i in range(n-1):
    cnt = 0
    for j in range(min(len(sorting_graph[i][1]), len(sorting_graph[i+1][1]))): # 작은 문자열 길이로 비교해야 함(아니면 index out of range)
        if sorting_graph[i][1][j] == sorting_graph[i+1][1][j]:
            cnt += 1
        else: # 한 번이라도 다르면 break(차피 앞에서 부터 차례로 보기 때문에)
            break 
    _max = max(cnt, _max) 
    length[sorting_graph[i][0]] = max(length[sorting_graph[i][0]], cnt) 
    length[sorting_graph[i+1][0]] = max(length[sorting_graph[i+1][0]], cnt)

flag = True
for i in range(n):
    if flag:
        if length[i] == _max:
            print(graph[i])
            flag = False
            pre = graph[i][:_max] # 접두사 저장
    else:
        if length[i] == _max and graph[i][:_max] == pre: # 접두사를 포함하는지 체크
            print(graph[i])
            break
