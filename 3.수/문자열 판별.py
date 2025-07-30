import sys
input = sys.stdin.readline

s = input().rstrip()
a = int(input())
graph = set()
for i in range(a):
    tmp = input().rstrip()
    graph.add(tmp)

d = [0 for _ in range(len(s))]
for i in range(len(s)):
    cur = s[i]

    if s[:i+1] in graph:
        d[i] = 1
    
    else: 
        for j in range(i):
            if d[j] == 1:
                if s[j+1:i+1] in graph:
                    d[i] = 1

print(d[len(s)-1])
