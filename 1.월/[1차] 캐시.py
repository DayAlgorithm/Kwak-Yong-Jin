def solution(cacheSize, cities):
    if cacheSize == 0:
        answer = 5 * len(cities)
        return answer
    cities = [c.lower() for c in cities]
    queue_dict = dict()
    cnt = 0
    answer = 0
    for city in cities:
        cnt += 1
        if len(queue_dict) < cacheSize: # cache가 비었을 때
            if not city in queue_dict: # cache에 없으면
                answer += 5
            else:
                answer += 1
            queue_dict[city] = cnt # 캐시에 들어간 시간 초기화
            
        else: # cache가 가득 찼을 때
            if not city in queue_dict: # cache에 없으면
                answer += 5 # 일단 5 증가
                tmp = min(queue_dict, key=queue_dict.get) # 가장 마지막에 사용된 도시 찾기
                queue_dict.pop(tmp) # 해당 도시 버리기
            else:
                answer += 1
            
            queue_dict[city] = cnt
            
    return answer
