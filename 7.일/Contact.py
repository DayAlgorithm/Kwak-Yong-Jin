import re
import sys
input = sys.stdin.readline

pattern = re.compile(r'(100+1+|01)+')
t = int(input())
for _ in range(t):
    s = input().strip()
    if pattern.fullmatch(s):
        print("YES")
    else:
        print("NO")
