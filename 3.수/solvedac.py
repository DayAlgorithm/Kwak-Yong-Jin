import sys
input = sys.stdin.readline

n = int(input())
if n == 0: # 입력이 0일 때
    print(0)
    exit()
cut = int(n * 0.15 + 0.5) # 파이썬의 round 함수는 짝수 쪽으로 반올림 하기 때문에
scores = sorted([int(input()) for _ in range(n)]) # 입력 받아서 오름차순 정렬
if cut == 0: # 절삭오차가 없으면 기존 리스트 그대로 쓰기
    filtered = scores
else:
    filtered = scores[cut:-cut] # 절삭오차 일어난 부분 자르기
if not filtered: # 리스트에 아무것도 없으면 0
    print(0)
else:
    print(int(sum(filtered)/len(filtered) + 0.5)) # 나온 결과도 반올림
