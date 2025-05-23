import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n = int(input())
c = [[] for i in range(n+1)]
d = [[0,0] for i in range(n+1)]

for _ in range(n-1):
    a,b = map(int , input().split())
    c[a].append(b)
    c[b].append(a)

visited = [0 for i in range(n+1)]
def dfs(start):
    global c
    global visited
    visited[start] = 1
    if len(c[start]) == 0:
        d[start][1] = 1
        d[start][0] = 0
    else:
        for i in c[start]:
            if visited[i] == 0:
                dfs(i)
                d[start][1] += min(d[i][0] , d[i][1])
                d[start][0] += d[i][1]
        d[start][1] += 1

dfs(1)
print(min(d[1][0],d[1][1]))
