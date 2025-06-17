import sys
input = sys.stdin.readline

n = int(input())

if n % 7 in (0, 2): # 주기로 반복
    print("CY")
else:
    print("SK")
