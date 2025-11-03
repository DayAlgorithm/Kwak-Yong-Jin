import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def dfs(num, cnt, n):
    if cnt == n:
        result.append(num)
        return

    for i in [1, 3, 5, 7, 9]:
        if is_prime(num*10 + i):
            dfs(num*10 + i, cnt+1, n)
    return

n = int(input())
result = []
for i in [2, 3, 5, 7]:
    dfs(i, 1, n)
print(*result, sep='\n')
