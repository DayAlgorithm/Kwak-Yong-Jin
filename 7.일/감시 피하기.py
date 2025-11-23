import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
graph = [list(input().split()) for _ in range(n)]
teachers = []
students = set()
nothings = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'T':
            teachers.append((i, j))
        elif graph[i][j] == 'S':
            students.add((i, j))
        else:
            nothings.append((i, j))

result = False
for combi in combinations(nothings, 3):
    for teacher in teachers:
        x, y = teacher

        flag = True # 학생 발견 X
        # x 증가 방향
        for i in range(x+1, n):
            if (i, y) in combi: # 장애물이 있으면
                break

            if (i, y) in students: # 학생을 발견하면
                flag = False
                break

        if flag == False:
            break

        # x 감소 방향
        for i in range(x-1, -1, -1):
            if (i, y) in combi:
                break
            if (i, y) in students:
                flag = False
                break
        
        if flag == False:
            break

        # y 증가 방향
        for i in range(y+1, n):
            if (x, i) in combi:
                break
            if (x, i) in students:
                flag = False
                break
        
        if flag == False:
            break

        # y 감소 방향
        for i in range(y-1, -1, -1):
            if (x, i) in combi:
                break
            if (x, i) in students:
                flag = False
                break
        
        if flag == False:
            break
    
    if flag:
        result = True
        break

if result:
    print('YES')
else:
    print('NO')
