from itertools import permutations

def solution(numbers):
    answer = 0
    graph = list(numbers)
    result = set()
    # 가능한 모든 조합의 정수 만들기
    for i in range(1, len(graph) + 1):
        p = list(permutations(graph, i))
        for j in p:
            s = int(''.join(map(str, j)))
            result.add(s)
    
    # 소수 판별하기
    result = list(result)
    while result:
        num = result.pop()
        if num == 0 or num == 1:
            continue
        
        end = int(num**(1/2))+1 # 마지막
        flag = True
        for i in range(2, end):
            if num%i == 0:
                flag = False
                break
        
        if flag:
            answer += 1
    
    return answer
