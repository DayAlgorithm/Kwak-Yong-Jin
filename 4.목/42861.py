def find(a, parents):
    if parents[a] != a:
        parents[a] = find(parents[a], parents)
    return parents[a]    

def union(a, b, parents):
    roota = find(a, parents)
    rootb = find(b, parents)
    
    if roota != rootb:
        parents[rootb] = roota
    
def solution(n, costs):
    answer = 0
    graph = []
    for i in range(len(costs)):
        a, b, c = costs[i]
        graph.append([c, a, b])
    graph.sort()
    parents = [i for i in range(n)]
    cnt = 0
    idx = 0
    while cnt != n-1:
        c, a, b = graph[idx] 
        if find(a, parents) != find(b, parents): 
            union(a, b, parents)
            answer += c
            cnt += 1
        idx += 1
    return answer
