```
def solution(edges):
    answer = [0, 0, 0, 0]

    new_edges = {}
    for a, b in edges:
        if not new_edges.get(a):
            new_edges[a] = [0, 0]
        if not new_edges.get(b):
            new_edges[b] = [0, 0]
        
        new_edges[a][0] += 1 # a정점 기준 나가는 간선
        new_edges[b][1] += 1 # b정점 기준 들어오는 간선
    
    for key, value in new_edges.items():
        if value[0] >= 2 and value[1] == 0: 하나도 안들어오고 2개 이상의 나가기만 하는 간선을 갖는 정점
            answer[0] = key
        
        elif value[0] == 0 and value[1] > 0: # 막대그래프
            answer[2] += 1
        
        elif value[0] >= 2 and value[1] >= 2: # 8자 그래프
            answer[3] += 1
    
    answer[1] = (new_edges[answer[0]][0] - answer[2] - answer[3]) # 도넛

    return answer
  ```
