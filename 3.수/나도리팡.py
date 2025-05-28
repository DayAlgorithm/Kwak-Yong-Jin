import sys
input = sys.stdin.readline

n,m,k = map(int,input().split())
numbers = list(map(int,input().split()))
numbers.sort()
for i in range(n):
    if numbers[0] == 0:
        numbers.pop(0)
count = 0
for i in range(k):
    if len(numbers) == 0:
        print("YES")
        break
    elif len(numbers) == 1:
        if numbers[0] < m:
            print("NO")
            break
        elif numbers[0] >= m:
            print("YES")
            break
    else:
        numbers[0] -= 1
        numbers[-1] += 1
        if numbers[0] == 0:
            numbers.pop(0)
        if numbers[-1] == m:
            numbers.pop()

else:
    if len(numbers) > 0:
        print("NO")
    else:
        print("YES")
