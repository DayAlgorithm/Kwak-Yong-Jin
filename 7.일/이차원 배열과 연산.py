import sys
from collections import defaultdict
input = sys.stdin.readline

r, c, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]
iter = 0

while True:
    if r <= len(graph) and c <= len(graph[0]):
        if graph[r-1][c-1] == q:
            print(iter)
            break

    if iter >= 101:
        print(-1)
        break

    iter += 1
    row_cnt = len(graph)
    col_cnt = len(graph[0])

    new_graph = []

    if row_cnt >= col_cnt: # R 연산
        for i in range(row_cnt):
            chk = defaultdict(int)
            for j in range(col_cnt):
                chk[graph[i][j]] += 1

            chk = list(chk.items())
            chk = sorted(chk, key=lambda x : (x[1], x[0]))
            tmp = []
            for k, v in chk:
                if k == 0: 
                    continue
                tmp.append(k)
                tmp.append(v)
            
            new_graph.append(tmp)
        
        cnt = -1
        for i in range(row_cnt):
            if cnt < len(new_graph[i]):
                cnt = len(new_graph[i])
        
        for i in range(row_cnt):
            while len(new_graph[i]) < cnt:
                new_graph[i].append(0)

        graph = new_graph

    else: # C 연산
        new_col = []
        for i in range(col_cnt):
            chk = defaultdict(int)
            for j in range(row_cnt):
                chk[graph[j][i]] += 1
            
            chk = list(chk.items())
            chk = sorted(chk, key=lambda x : (x[1], x[0]))
            tmp = []
            for k, v in chk:
                if k == 0:
                    continue
                tmp.append(k)
                tmp.append(v)
            
            new_col.append(tmp)
    
    # C graph 만들어주기
        cnt = -1
        for i in range(col_cnt):
            if cnt < len(new_col[i]):
                cnt = len(new_col[i])

        new_graph = [[0 for _ in range(col_cnt)] for _ in range(cnt)]
        for i in range(col_cnt):
            while len(new_col[i]) < cnt:
                new_col[i].append(0)

            for j in range(cnt):
                new_graph[j][i] = new_col[i][j]
        
        graph = new_graph      
