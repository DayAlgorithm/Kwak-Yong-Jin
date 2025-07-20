import sys
input = sys.stdin.readline

s = input().strip()

if s != s[::-1]:
    print(len(s))
else:
    if s[1:] != s[1:][::-1] or s[:-1] != s[:-1][::-1]:
        print(len(s) - 1)
    else:
        print(-1)
