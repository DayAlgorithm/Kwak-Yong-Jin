def solution(s):
    s = list(s)
    stack = []
    while s:
        cur = s.pop()
        if cur == '(':
            if not stack:
                return False
            if stack[-1] == ')':
                stack.pop()
            
        else:
            stack.append(cur)
    
    if stack:
        return False    
    
    return True
    
