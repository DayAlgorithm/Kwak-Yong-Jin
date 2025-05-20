import sys
input = sys.stdin.readline
MOD = 10**8

c = int(input())
for _ in range(c):
    s, n, t, l = input().split()
    n, t, l = int(n), int(t), int(l)

    if s == "O(N)":
        tmp = -(-(n * t) // MOD) # float로 처리하면 overflow 발생해서 음수로 변환하고 정수 나눗셈
        if tmp > l:
            print("TLE!")
        else:
            print("May Pass.")
    elif s == "O(2^N)":
        tmp = -(-(2**n * t) // MOD)
        if tmp > l:
            print("TLE!")
        else:
            print("May Pass.")
    elif s == "O(N!)":
        tmp = 1
        flag = True
        for i in range(n, 0, -1):
            tmp *= i
            ret = -(-(tmp * t) // MOD)
            if ret > l:
                flag = False
                break
        if flag:
            print("May Pass.")
        else:
            print("TLE!")
    elif s == "O(N^2)":
        tmp = -(-(n**2 * t) // MOD)
        if tmp > l:
            print("TLE!")
        else:
            print("May Pass.")
    elif s == "O(N^3)":
        tmp = -(-(n**3 * t) // MOD)
        if tmp > l:
            print("TLE!")
        else:
            print("May Pass.")
