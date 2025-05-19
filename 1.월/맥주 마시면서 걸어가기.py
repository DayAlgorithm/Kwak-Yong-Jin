import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())

    graph = {} # 모든 노드를 dict으로 저장
    stx, sty = map(int, input().rstrip().split())
    graph[(stx, sty)] = []

    for _ in range(n):
        graph[tuple(map(int, input().rstrip().split()))] = []

    dstx, dsty = map(int, input().rstrip().split())
    graph[(dstx, dsty)] = []

    for node1 in graph.keys():
        for node2 in graph.keys():
            if node1 == node2:
                continue
            dis = abs((node2[0] - node1[0])) + abs((node2[1] - node1[1])) # 연결 가능한 노드끼리 저장
            if dis <= 1000:
                graph[node1].append(node2)
                graph[node2].append(node1)
                
    visited = set()
    queue = deque()
    st = (stx, sty)
    queue.append(st)
    visited.add(st)
    
    flag = False
    while queue:
        cur = queue.popleft()
        if cur == (dstx, dsty):
            print("happy")
            flag = True
            break
        for node in graph[cur]:
            if not node in visited:
                visited.add(node)
                queue.append(node)
    if not flag:
        print("sad")
    
