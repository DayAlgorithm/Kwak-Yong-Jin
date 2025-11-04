import sys
input = sys.stdin.readline

n, x = map(int, input().split())
pati = [0] * (n + 1)
size = [0] * (n + 1)
pati[0] = 1
size[0] = 1

for i in range(1, n + 1):
    size[i] = size[i - 1] * 2 + 3
    pati[i] = pati[i - 1] * 2 + 1

def eat(level, x):
    if level == 0:
        return 1 if x >= 1 else 0
    elif x == 1:
        return 0
    elif x <= 1 + size[level - 1]:
        return eat(level - 1, x - 1)
    elif x == 2 + size[level - 1]:
        return pati[level - 1] + 1
    elif x <= 2 + size[level - 1] * 2:
        return pati[level - 1] + 1 + eat(level - 1, x - 2 - size[level - 1])
    else:
        return pati[level]

print(eat(n, x))
