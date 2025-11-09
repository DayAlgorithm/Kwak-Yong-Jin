import sys
input = sys.stdin.readline

n, k = map(int, input().split())
graph = list(map(int, input().split()))
diff = []

for i in range(n-1):
    diff.append(graph[i+1] - graph[i])
diff.sort()

answer = sum(diff[:(n-k)])
print(answer)
