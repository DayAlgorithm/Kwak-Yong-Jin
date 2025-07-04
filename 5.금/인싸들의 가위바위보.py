import sys
from itertools import permutations
input = sys.stdin.readline

N, K = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
ky = list(map(int, input().split()))
mh = list(map(int, input().split()))
jmove = [i + 1 for i in range(N)]

def dfs(p1, p2, idx, wins, players):
    global result
    if wins[0] == K:
        result = 1
        return
    if wins[1] == K or wins[2] == K:
        return
    if idx[0] == N:
        return

    p3 = 3 - (p1 + p2)
    m1 = players[p1][idx[p1]] - 1
    m2 = players[p2][idx[p2]] - 1
    idx[p1] += 1
    idx[p2] += 1

    if graph[m1][m2] == 2 or (graph[m1][m2] == 1 and p1 > p2):
        wins[p1] += 1
        dfs(p1, p3, idx, wins, players)
    elif graph[m1][m2] == 0 or (graph[m1][m2] == 1 and p1 < p2):
        wins[p2] += 1
        dfs(p2, p3, idx, wins, players)

for jorder in permutations(jmove, N):
    players = [jorder, ky, mh]
    idx = [0, 0, 0]
    wins = [0, 0, 0]
    result = 0
    dfs(0, 1, idx, wins, players)
    if result == 1:
        print(1)
        break
else:
    print(0)
