import sys
from bisect import bisect_left
input = sys.stdin.readline

N, H = map(int, input().split())
understone = []
overstone = []
for i in range(1, N+1):
    height = int(input())
    if i%2: # 홀수이면 석순 -> understone
        understone.append(height)
    else:
        overstone.append(height)

understone.sort()
overstone.sort()

result = [0 for _ in range(H+1)] # 각 높이별로 몇 개의 장애물을 부숴야 하는지 기록
for i in range(1, H+1):
    # understone
    tmp = bisect_left(understone, i) # i번째 높이가 들어갈 위치 찾기
    result[i] += (len(understone) - tmp)

    # overstone
    over_height = (H+1) - i
    tmp = bisect_left(overstone, over_height)
    result[i] += (len(overstone) - tmp)

print(min(result[1:]), result[1:].count(min(result[1:])))
