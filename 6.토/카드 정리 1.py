import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
check = [0] * m
ret = 0
joker = False # 조커 사용 여부 확인
for i in range(n):
    cnt = 0
    contain = []
    for j in range(m):
        if graph[i][j] != 0: # 박스에 몇개의 색상의 카드가 들어있는지 확인
            cnt += 1
            contain.append(j)
    
    if cnt >= 2: # 한 박스에 카드 색이 2개 이상이면
        if joker == False:
            joker = True
        else:
            ret += 1
    
    elif cnt == 1: # 만약 색 하나만 있는데, 그 색의 종류가 처음 나오면 그 박스를 그 색상의 카드를 몰아주는 박스로 지정
        if check[contain[0]] == 0:
            check[contain[0]] = 1
        else: # 아니면 +1
            ret += 1

if joker == False: # 만약 조커가 한 번도 안 쓰였으면
    ret = max(0, ret-1)
print(ret)
