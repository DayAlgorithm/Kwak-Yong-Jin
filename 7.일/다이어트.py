import sys
input = sys.stdin.readline

g = int(input())
answer = []
for i in range(1, 100001):
    tmp = i**2 - g
    if tmp <= 0: continue
    else:
        post = int(tmp**0.5)
        if post*post == tmp and post > 0: # int로 변환해서 제곱한 값과 그 전의 값이 같아야 함
            answer.append(i)
if answer:
    print(*answer, sep='\n')
else:
    print(-1)
