import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = input().strip()

arr = [0] * n
result = [0] * n
min_liar = float('inf')

# 'H': 1, 'L': 0, '?': -1
for i in range(n):
    if s[i] == 'H':
        arr[i] = 1
    elif s[i] == 'L':
        arr[i] = 0
    else:
        arr[i] = -1

def dfs(idx, liar):
    global min_liar

    if liar >= min_liar:
        return
    if idx >= n:
        # 마지막 사람이 말 안했으면 무조건 가능
        if arr[n - 1] == -1:
            min_liar = min(min_liar, liar)
            return
        # 마지막 사람이 정직
        if result[n - 1]:
            if arr[n - 1] == result[0]:
                min_liar = min(min_liar, liar)
        else:
            if arr[n - 1] != result[0]:
                min_liar = min(min_liar, liar)
        return

    # 이전 사람이 말 안했을 경우 → 자유롭게 분기
    if arr[idx - 1] == -1:
        result[idx] = 1
        dfs(idx + 1, liar)
        result[idx] = 0
        dfs(idx + 1, liar + 1)
        return

    # 이전 사람이 정직이면 다음 사람의 상태는 arr[idx - 1] 그대로
    if result[idx - 1]:
        result[idx] = arr[idx - 1]
    else:
        result[idx] = 1 - arr[idx - 1]  # 거짓말

    if result[idx] == 0:
        liar += 1
    dfs(idx + 1, liar)

# 시작사람이 거짓 (0)
result[0] = 0
dfs(1, 1)

# 시작사람이 정직 (1)
result[0] = 1
dfs(1, 0)

print(min_liar if min_liar != float('inf') else -1)
