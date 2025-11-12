import sys
input = sys.stdin.readline

n = int(input())
pd1, pd2, pd3 = 0, 0, 0
md1, md2, md3 = 0, 0, 0
for i in range(n):
    a, b, c = map(int, input().split())
    if i == 0:
        pd1 = a
        pd2 = b
        pd3 = c

        md1 = a
        md2 = b
        md3 = c
        continue

    ppd1 = max(pd1, pd2) + a
    ppd2 = max(pd1, pd2, pd3) + b
    ppd3 = max(pd2, pd3) + c

    pd1 = ppd1
    pd2 = ppd2
    pd3 = ppd3

    mmd1 = min(md1, md2) + a
    mmd2 = min(md1, md2, md3) + b
    mmd3 = min(md2, md3) + c

    md1 = mmd1
    md2 = mmd2
    md3 = mmd3

print(max(pd1, pd2, pd3), min(md1, md2, md3))
