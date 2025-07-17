import sys
input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))
result = [0]*n

for i in range(n):
    max_slope = float('-inf')
    for j in range(i+1, n):
        s = (h[j]-h[i])/(j-i)
        if s > max_slope:
            max_slope = s
            result[i] += 1

    min_slope = float('inf')
    for j in range(i-1, -1, -1):
        s = (h[j]-h[i])/(j-i)
        if s < min_slope:
            min_slope = s
            result[i] += 1

print(max(result))
