import sys
input = sys.stdin.readline

matches = [(i, j) for i in range(6) for j in range(i+1, 6)]

def dfs(idx):
    if idx == 15:
        return all(all(x == 0 for x in team) for team in result)

    a, b = matches[idx]

    if result[a][0] > 0 and result[b][2] > 0:
        result[a][0] -= 1
        result[b][2] -= 1
        if dfs(idx + 1):
            return True
        result[a][0] += 1
        result[b][2] += 1

    if result[a][1] > 0 and result[b][1] > 0:
        result[a][1] -= 1
        result[b][1] -= 1
        if dfs(idx + 1):
            return True
        result[a][1] += 1
        result[b][1] += 1

    if result[a][2] > 0 and result[b][0] > 0:
        result[a][2] -= 1
        result[b][0] -= 1
        if dfs(idx + 1):
            return True
        result[a][2] += 1
        result[b][0] += 1

    return False


answers = []
for _ in range(4):
    data = list(map(int, input().split()))
    result = [data[i*3:(i+1)*3] for i in range(6)]

    if any(sum(team) != 5 for team in result):
        answers.append(0)
        continue

    answers.append(1 if dfs(0) else 0)

print(*answers)
