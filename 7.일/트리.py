import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(node, parent): # dfs에서 이전 노드를 같이 줘서 이전 노드로 역행하는지 확인 True면 사이클
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            if dfs(neighbor, node):
                return True
        elif neighbor != parent:
            return True
    return False

case_num = 0

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    tree_count = 0

    for i in range(1, n + 1):
        if not visited[i]:
            has_cycle = dfs(i, -1)
            if not has_cycle:
                tree_count += 1

    case_num += 1
    if tree_count == 0:
        print(f"Case {case_num}: No trees.")
    elif tree_count == 1:
        print(f"Case {case_num}: There is one tree.")
    else:
        print(f"Case {case_num}: A forest of {tree_count} trees.")
