import math

def solution(brown, yellow):
    answer = []
    S = (brown + 4) / 2
    P = brown + yellow
    D = math.sqrt(S*S - 4*P)
    x = int((S + D) / 2)
    y = int((S - D) / 2)
    answer.append(x)
    answer.append(y)
    return answer
