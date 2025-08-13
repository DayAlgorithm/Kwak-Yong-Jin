import sys
input = sys.stdin.readline

def solve(n):
    if n in A:
        return A[n]
    A[n] = solve(n // P) + solve(n // Q)
    return A[n]

N, P, Q = map(int, input().split())
A = {0: 1}

print(solve(N))
