import sys
input = sys.stdin.readline

n = int(input())
mp, mf, ms, mv = map(int, input().split())
foods = [None] + [list(map(int, input().split())) for _ in range(n)]  # 1-indexed

min_cost = float('inf')
best_set = []

def dfs(idx, p, f, s, v, cost, selected):
    global min_cost, best_set

    if p >= mp and f >= mf and s >= ms and v >= mv:
        if cost < min_cost:
            min_cost = cost
            best_set = selected[:]
        elif cost == min_cost:
            best_set = min(best_set, selected)
        return

    if idx > n:
        return

    # 선택하지 않는 경우
    dfs(idx + 1, p, f, s, v, cost, selected)

    # 선택하는 경우
    np, nf, ns, nv, c = foods[idx]
    dfs(idx + 1, p + np, f + nf, s + ns, v + nv, cost + c, selected + [idx])

dfs(1, 0, 0, 0, 0, 0, [])

if min_cost == float('inf'):
    print(-1)
else:
    print(min_cost)
    print(*best_set)
