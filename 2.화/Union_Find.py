import sys
input = sys.stdin.readline

def find(a):
    root = a
    while graph[root] != root:
        root = graph[root]
    
    while graph[a] != root:
        next_node = graph[a]
        graph[a] = root
        a = next_node
        
    return root

def union(a, b):
    a_parent = find(a)
    b_parent = find(b)
    if a_parent != b_parent:
        if a_parent < b_parent:
            graph[b_parent] = a_parent
        else:
            graph[a_parent] = b_parent

n, m = map(int, input().split())
graph = [i for i in range(n + 1)]

for _ in range(m):
    k, a, b = map(int, input().split())
    if k == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
