import sys
from itertools import combinations
input = sys.stdin.readline

n, k = map(int, input().split())
words = [list(input().rstrip()) for _ in range(n)]
if k < 5:
    print(0)
    sys.exit(0)

k -= 5
kinds = [] # 한 번 걸러낸 문자 
mix = set()
for word in words:
    tmp = set(word) - set('antic')
    tmp = list(tmp)
    for i in tmp:
        mix.add(i)
    kinds.append(tmp)

mix = list(mix)
k = min(k, len(mix)) 

result = [0]
for c in combinations(mix, k):
    c = set(c)
    cnt = 0
    for i in kinds:
        flag = True
        for j in i:
            if j in c:
                continue
            else:
                flag = False
                break
        if flag:
            cnt += 1
    result.append(cnt)
print(max(result))
