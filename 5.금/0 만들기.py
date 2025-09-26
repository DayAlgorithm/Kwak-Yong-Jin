import sys
input = sys.stdin.readline

def solve(cnt, equation):
    if cnt == n:
        new_equation = equation.replace(' ', '')
        cnt = 0
        num = ''
        pos = '' # 이전 연산자
        pos_num = 0 # 이전 숫자
        for char in new_equation:
            if not char in '+-':
                num += char
            else:
                if pos == '':
                    pos = char
                    pos_num = int(num)
                    num = ''
                else:
                    if pos == '+':
                        pos_num += int(num)
                    else:
                        pos_num -= int(num)
                    pos = char
                    num = '' 
        
        if pos == '+':
            pos_num += int(num)
        elif pos == '-':
            pos_num -= int(num)

        if num != '' and pos == '':
            pos_num = int(num)
        if pos_num == 0:
            result.append(equation)
        return
    solve(cnt + 1, equation + '+' + str(arr[cnt]))
    solve(cnt + 1, equation + '-' + str(arr[cnt]))
    solve(cnt + 1, equation + ' ' + str(arr[cnt]))

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [i for i in range(1, n+1)]

    result = []

    solve(1, str(arr[0]))

    result.sort()
    print(*result, sep='\n')
    print()
