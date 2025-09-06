def solution(number, k):
    cnt = 0
    stack = [number[0]]
    
    for i in range(1, len(number)):
        if cnt >= k: # 더 이상 숫자를 제거하지 못하면 계속 추가만 함
            stack.append(number[i])
            continue
            
        if stack[-1] >= number[i]:
            stack.append(number[i])
        
        else:
            while stack and stack[-1] < number[i]:
                stack.pop()
                cnt += 1
                if cnt >= k:
                    break
            stack.append(number[i])
            
    while cnt < k:
        stack.pop()
        cnt += 1
        
    answer = ''.join(map(str, stack))
    return answer
