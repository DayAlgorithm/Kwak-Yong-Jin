import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
graph = list(map(int, input().split()))
answer = 0
for permu in permutations(graph, n):
    tmp = 0
    for i in range(n-1):
        tmp += abs(permu[i] - permu[i+1])
    if tmp > answer:
        answer = tmp
print(answer)
