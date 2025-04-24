def solution(cap, n, deliveries, pickups):
    answer = 0
    d = p = 0

    for i in range(n-1, -1, -1):  
        d += deliveries[i]
        p += pickups[i]
        
        while d > 0 or p > 0: # 한 번 갈때 최대치를 들고오고, 최대치를 가져감
            d -= cap
            p -= cap
            answer += (i+1) * 2
    return answer
