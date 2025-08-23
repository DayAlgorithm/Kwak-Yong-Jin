import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()
s3 = input().strip()

n1, n2, n3 = len(s1), len(s2), len(s3)
d = [[[0] * (n3 + 1) for _ in range(n2 + 1)] for __ in range(n1 + 1)]

for i in range(1, n1 + 1):
    for j in range(1, n2 + 1):
        for k in range(1, n3 + 1):
            if s1[i-1] == s2[j-1] == s3[k-1]:
                d[i][j][k] = d[i-1][j-1][k-1] + 1
            else:
                d[i][j][k] = max(
                    d[i-1][j][k],
                    d[i][j-1][k],
                    d[i][j][k-1]
                )

print(d[n1][n2][n3])
