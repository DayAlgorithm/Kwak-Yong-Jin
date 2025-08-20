from collections import deque
def bfs(x, cnt, target, words, visited):
    queue = deque()
    queue.append((x, cnt))
    
    while queue:
        s1, cnt = queue.popleft()
        if s1 == target:
            return cnt
        for i in range(len(words)):
            s2 = words[i]
            diff_count = sum(c1 != c2 for c1, c2 in zip(s1, s2))
            if diff_count == 1:
                if visited[i] == 0:
                    queue.append((s2, cnt + 1))
            
def solution(begin, target, words):
    answer = 0
    visited = [0] * (len(words))
    
    flag = False
    num = 0
    for i in range(len(words)):
        if target == words[i]:
            flag = True
            num = i
            break
            
    if flag: # words 안에 target이 있을때만 시작
        answer = bfs(begin, 0, target, words, visited)
    return answer
