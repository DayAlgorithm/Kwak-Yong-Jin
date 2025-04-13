import heapq 

def solution(scoville, K):
    heapq.heapify(scoville) # scoville 배열을 바로 heapq로 변환
    answer = 0
    while True:
        _min1 = heapq.heappop(scoville)
        if _min1 >= K: # 가장 안 매운 음식의 스코빌 지수 확인
            break
        if len(scoville) == 0: # 만약 가장 안 매운 음식이 마지막 음식이었다면 못만듬
            answer = -1
            break
        answer += 1
        _min2 = heapq.heappop(scoville)
        tmp = _min1 + _min2 * 2
        heapq.heappush(scoville, tmp) # 섞고 추가
    return answer
