import sys
input = sys.stdin.readline

n = int(input())
stack = []
answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y == 0: 
        answer += len(stack)
        stack = []
        continue

    if not stack or stack[-1] < y:
        stack.append(y)
        continue

    if stack[-1] == y:
        continue

    if stack[-1] > y:
        while True:
            answer += 1
            stack.pop()

            if not stack:
                stack.append(y)
                break

            if stack[-1] == y:
                break

            if stack[-1] < y:
                stack.append(y)
                break
answer += len(stack)
print(answer)
