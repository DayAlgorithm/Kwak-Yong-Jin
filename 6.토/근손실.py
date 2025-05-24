import sys
input = sys.stdin.readline

def dfs(start, n, visited):
    global cnt
    if n == 0:
        cnt += 1
        return
    
    if start < 500:
        return

    for idx, kit in kits:
        if visited[idx] == 1:
            continue
        next = start + kit - k
        visited[idx] = 1
        dfs(next, n-1, visited)
        visited[idx] = 0

n, k = map(int, input().split())
A = list(map(int, input().split()))
kits = []
for i in range(len(A)):
    kits.append([i+1, A[i]])
start = 500
cnt = 0
visited = [0] * (len(A) + 1)

dfs(start, n, visited)
print(cnt)
