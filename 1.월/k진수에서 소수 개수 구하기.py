import math

def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    lim = int(math.isqrt(x))
    for i in range(2, lim+1):
        if x % i == 0:
            return False
    return True

def solution(n: int, k: int) -> int:
    s = ''
    tmp = n
    if tmp == 0:
        s = '0'
    while tmp > 0:
        s = str(tmp % k) + s
        tmp //= k
    
    parts = s.split('0')
    
    count = 0
    for part in parts:
        if part == '':
            continue
        if '0' in part:
            continue
        num = int(part)
        if is_prime(num):
            count += 1
    
    return count
