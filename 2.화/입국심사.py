import sys
input = sys.stdin.readline

n, m = map(int, input().split())
stations = [int(input()) for _ in range(n)]
start = 1
end = max(stations) * m

while start <= end:
    mid = (start + end) // 2
    total = 0
    for station in stations:
        total += mid//station

    if total >= m:
        end = mid - 1
        
    else:
        start = mid + 1

print(start)
