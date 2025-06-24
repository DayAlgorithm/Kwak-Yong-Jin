import sys
from collections import defaultdict

input = sys.stdin.readline

def find_case(pizza):
    n = len(pizza)
    case = defaultdict(int)
    extended = pizza * 2  
    for size in range(1, n): 
        curr_sum = sum(extended[:size])
        case[curr_sum] += 1
        for i in range(1, n):
            curr_sum = curr_sum - extended[i-1] + extended[i+size-1]
            case[curr_sum] += 1
    case[sum(pizza)] += 1 
    return case

k = int(input())
n, m = map(int, input().split())
p1 = [int(input()) for _ in range(n)]
p2 = [int(input()) for _ in range(m)]

tmp1 = find_case(p1)
tmp2 = find_case(p2)

result = tmp1.get(k, 0) + tmp2.get(k, 0)
for num in tmp1:
    if k - num in tmp2:
        result += tmp1[num] * tmp2[k - num]

print(result)
