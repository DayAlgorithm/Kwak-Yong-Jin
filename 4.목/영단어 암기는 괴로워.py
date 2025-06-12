import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
dic = defaultdict(int)
for i in range(n):
    s = input().rstrip()

    if len(s) < m: # 길이 m 이하면 안외움
        continue
    
    dic[s] += 1

for k, v in dic.items():
    lengtho = len(k)
    graph.append([v, lengtho, k]) # 길이까지 포함해서 우선순위대로 저장

graph = sorted(graph, key=lambda x : (-x[0], -x[1], x[2])) # 람다함수로 저장

for i in range(len(graph)):
    v, lengtho, k = graph[i]
    print(k)
