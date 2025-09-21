import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    phones = [input().strip() for _ in range(n)]
    phones.sort()
    is_consistent = True
    for i in range(n - 1):
        if phones[i + 1].startswith(phones[i]):
            is_consistent = False
            break
    
    print("YES" if is_consistent else "NO")
