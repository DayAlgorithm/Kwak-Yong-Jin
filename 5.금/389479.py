def solution(players, m, k):
    answer = 0
    servers = [1] * (len(players))
    for i in range(len(players)):
        cur = players[i]
        ability = servers[i] * m
        if ability > cur: # 수용 가능
            continue
        else:
            need = (cur-ability)//m + 1
            answer += need
            for j in range(i, i+k): # 서버 수 증가시켜주기
                if j == len(servers): # 넘치면 멈추기
                    break
                servers[j] += need       
    return answer
