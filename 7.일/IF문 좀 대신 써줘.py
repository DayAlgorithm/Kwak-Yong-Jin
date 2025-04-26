import sys
from bisect import bisect_left 
input = sys.stdin.readline

n, m = map(int, input().split())
rank_name = []
scores = []
for _ in range(n):
    r, s = input().rstrip().split()
    rank_name.append(r)
    scores.append(int(s))

for _ in range(m):
    score = int(input())
    loc = bisect_left(scores, score) # 왼쪽부터 이분탐색해서 나온 결과가 그 친구의 칭호임
    print(rank_name[loc])
