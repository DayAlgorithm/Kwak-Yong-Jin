def solution(fees, records):
    answer = []
    result = dict()
    cars = dict()
    
    for record in records:
        t, n, f = record.split(' ') # time, number, flag
        h, m = t.split(':')
        t_m = int(m) + int(h) * 60 # total minutes
        
        if f == 'IN':
            cars[n] = t_m # 주차 시작 시각
            
        else:
            t_m = t_m - cars[n] # 총 주차 시간
            if n in result:
                result[n] += t_m
            else:
                result[n] = t_m

            cars[n] = -1
    
    for n, t_m in cars.items():
        if t_m != -1: # 출차 기록이 없는 경우
            t_m = (23 * 60 + 59) - t_m
            if n in result:
                result[n] += t_m
            else:
                result[n] = t_m
    
    for n in sorted(result.keys()):
        t_m = result[n]
        if t_m <= fees[0]: # 기본 시간 이하
            answer.append(fees[1])
        else:
            extra = t_m - fees[0]
            if extra % fees[2] == 0:
                answer.append(fees[1] + (extra // fees[2]) * fees[3])
            else:
                answer.append(fees[1] + (extra // fees[2] + 1) * fees[3])
    
    return answer
