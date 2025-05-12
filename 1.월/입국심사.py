def solution(n, times): 
    max_time = min(times) * n 
    start, end = 0, max_time
    while start <= end: # 시간으로 이분탐색
        mid = (start+end)//2
        total = 0
        for i in range(len(times)): # 해당 시간에 가능 인원 구하기
            total += mid//times[i]
        
        if total >= n: 
            end = mid-1
        else:
            start = mid+1

    answer = start
    return answer
