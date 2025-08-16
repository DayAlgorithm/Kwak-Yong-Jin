from bisect import bisect_left

def solution(graph):
    answer = 0
    graph.sort()
    result = [0]
    for i in range(graph[-1]+1):
        tmp = bisect_left(graph, i)
        if i <= len(graph) - tmp:
            result.append(i)
            
    answer = max(result)        
    return answer
