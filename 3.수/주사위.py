import sys
input = sys.stdin.readline

n = int(input())
dices = list(map(int, input().split()))

if n == 1:
    dices.sort()
    print(sum(dices[:5]))
else:
    _min = [
        min(dices[0], dices[5]),
        min(dices[1], dices[4]),
        min(dices[2], dices[3])
    ]
    
    _min.sort()
    min1 = _min[0]
    min2 = _min[0] + _min[1]
    min3 = _min[0] + _min[1] + _min[2]
    n3 = 4 
    n2 = 4 * (n - 2) + 4 * (n - 1)
    n1 = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    ans = (n1 * min1) + (n2 * min2) + (n3 * min3)
    print(ans)
