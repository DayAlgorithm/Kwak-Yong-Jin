import sys
input = sys.stdin.readline

N = int(input())
left_counts = list(map(int, input().split()))
result = [0] * N  

for i in range(N):
    cnt = left_counts[i]
    for j in range(N):
        if result[j] == 0:  
            if cnt == 0:
                result[j] = i + 1
                break
            cnt -= 1

print(*result)
