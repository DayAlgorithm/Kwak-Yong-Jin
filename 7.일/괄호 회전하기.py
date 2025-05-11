from collections import deque 
def solution(s):
    s = deque(list(s))
    rep = len(s)
    stack = []
    answer = 0
    tmp = [')', '}', ']']
    for _ in range(rep):
        flag = True # stack이 비었는데 열리는 괄호 들어가면 False
        for i in range(rep-1, -1, -1): # 거꾸로 돌면서 시작
            cur = s[i]
            if cur in tmp: # 닫히는 괄호는 계속 넣어도 됨
                stack.append(cur)
                continue
            if stack: 
                if cur == '(' and stack[-1] == ')':
                    stack.pop()
                elif cur == '[' and stack[-1] == ']':
                    stack.pop()
                elif cur == '{' and stack[-1] == '}':
                    stack.pop()
            else:
                flag = False
                break

        if len(stack) == 0 and flag:
            answer += 1
        swp = s.popleft()
        s.append(swp)        

    return answer
