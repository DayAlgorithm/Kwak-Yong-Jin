import sys
sys.setrecursionlimit(10000)

num = 0
n = 0
cache = [dict() for _ in range(9)] 

def dp(cnt, now):
    if cnt > 8:
        return float('inf')
    if now == num:
        return cnt
    
    if now in cache[cnt]:
        return cache[cnt][now]
    
    ret = float('inf')
    next_num = 0
    for i in range(9 - cnt):
        next_num = next_num * 10 + n 
        ret = min(ret, dp(cnt + 1 + i, now + next_num))
        ret = min(ret, dp(cnt + 1 + i, now - next_num))
        ret = min(ret, dp(cnt + 1 + i, now * next_num))
        if next_num != 0:
            ret = min(ret, dp(cnt + 1 + i, now // next_num))
    
    cache[cnt][now] = ret
    return ret

def solution(N, number):
    global n, num, cache
    n, num = N, number
    cache = [dict() for _ in range(9)]  
    ans = dp(0, 0)
    return -1 if ans == float('inf') else ans
