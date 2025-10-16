import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

low = max(arr)
high = sum(arr)
result = high

while low <= high:
    mid = (low + high) // 2
    count = 1
    total = 0
    for x in arr:
        if total + x > mid:
            count += 1
            total = x
        else:
            total += x
        
    if count > m:
        low = mid + 1
    else:
        answer = mid
        high = mid - 1
    
print(answer)
