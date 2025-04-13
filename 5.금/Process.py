```
from collections import deque # 파이썬은 queue를 deque로 구현

def solution(priorities, location):
    cnt = 0 # 실행 횟수 세기
    tmp = chr(65 + location) # 목표 값의 대문자 영어 찾기
    new_pri = [] # 우선순위와 대문자를 같이 저장
    for i in range(len(priorities)):
        new_pri.append([priorities[i], chr(65 + i)])
    queue = deque(new_pri) 
    while queue:
        p, k = queue.popleft()
        if len(queue) == 0: # queue에 데이터가 하나 들어있을 경우 빈칸이 되는 예외가 있음
            cnt += 1
            answer = cnt
            break
        elif p >= max(queue)[0]: # queue 내부의 우선순위의 최댓값과 비교해서 더 크거나 같으면 실행
            cnt += 1 
            if k == tmp:
                answer = cnt
                break
        else:
            queue.append([p, k]) # 실행되지 못한 프로세스는 다시 삽입

    return answer
  ```
