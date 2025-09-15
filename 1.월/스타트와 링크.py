from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
cases = list(combinations(range(n), int(n//2)))
result = sys.maxsize
for case in cases:
    start = 0
    link = 0

    for i in range(n):
        for j in range(n):
            if i in case and j in case:
                start += graph[i][j]
            elif i not in case and j not in case:
                link += graph[i][j]
    result = min(result, abs(start - link))

    if result == 0:
        print(0)
        exit(0)

print(result)
