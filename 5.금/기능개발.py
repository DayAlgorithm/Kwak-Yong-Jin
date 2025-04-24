from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    day = 0
    while progresses:
        cnt = 0
        progresses[0] += day*speeds[0]                                # 현재 날짜 기준으로 작업 진도 업데이트
        day += int((100 - progresses[0])/speeds[0]+0.5)               # 지금 날짜 기준으로 우선순위가 높은 작업을 끝내는데 걸리는 일수 계산
        if day*speeds[0] + progresses[0] < 100:
            day += 1
        while progresses and progresses[0] + day*speeds[0] >= 100:    # 100의 작업 진도가 넘은 작업들 전부 제거
            progresses.popleft()
            speeds.popleft()
            cnt += 1
        answer.append(cnt)
    return answer
