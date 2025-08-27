from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    queue = deque(people)
    while queue:
        if len(queue) == 1:
            answer += 1
            queue.pop()
        
        elif queue[-1] + queue[0] <= limit:
            answer += 1
            queue.popleft()
            queue.pop()
            
        else:
            answer += 1
            queue.pop()
    
    return answer
