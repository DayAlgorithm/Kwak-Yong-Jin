def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, cur in enumerate(prices):
        while stack and stack[-1][0] > cur:
            tmp, t = stack.pop()
            answer[t] = i - t
        stack.append([cur, i])
    
    while stack:
        tmp, t = stack.pop()
        answer[t] = len(prices) - 1 - t
        
    return answer
