import sys
input = sys.stdin.readline

def dfs(n, ret):
    if n == 0:                         # n==0이면 합침
        result.append(''.join(ret))
        return
    
    if n < 0:                          # n이 음수면 불가능 한 경우임
        return
 
    if n >= 1:                         # 여기서부터 n이 1,2,3이면 바로 끝낼 수 있는 경우와 그렇지 않은 경우 나눠서 추가
        ret.append('1') 
        if n == 1:
            dfs(n-1, ret)
        else:
            ret.append('+')
            dfs(n-1, ret)
            ret.pop()
        ret.pop()

    if n >= 2:
        ret.append('2')
        if n == 2:
            dfs(n-2, ret)
        else:
            ret.append('+')
            dfs(n-2, ret)
            ret.pop()
        ret.pop()

    if n >= 3:
        ret.append('3')
        if n == 3:
            dfs(n-3, ret)
        else:
            ret.append('+')
            dfs(n-3, ret)
            ret.pop()
        ret.pop()

n, k = map(int, input().split())
result = []
ret = []
dfs(n, ret)

result.sort()

if k <= len(result):
    print(result[k-1])
else:
    print(-1)
