import sys
from collections import defaultdict
input = sys.stdin.readline

def chk(st):
    flag = True
    for i in range(1, len(st)- 1):
        if st[i-1] == st[i] or st[i] == st[i+1]:
            flag = False
    
    if flag:
        return 1
    else:
        return 0
    
def dfs(st, end, kinds, words):
    global answer
    if len(st) == end:
        answer += chk(st)
        return
    
    for kind in kinds:
        if st[-1] != kind and words[kind] != 0:
            words[kind] -= 1
            dfs(st + kind, end, kinds, words)
            words[kind] += 1
    
    return

s = list(input().rstrip())
end = len(s)
words = defaultdict(int)
kinds = set()
for i in s:
    words[i] += 1
    kinds.add(i)

answer = 0
kinds = list(kinds)
for kind in kinds:
    tmp = ''
    words[kind] -= 1
    dfs(tmp + kind, end, kinds, words)
    words[kind] += 1
print(answer)
