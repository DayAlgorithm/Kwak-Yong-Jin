from functools import cmp_to_key

def compare(x, y):
    # 두 수를 문자열로 변환 후 이어붙여서 비교
    if str(x) + str(y) > str(y) + str(x):
        return -1  # x가 앞으로
    elif str(x) + str(y) < str(y) + str(x):
        return 1   # y가 앞으로
    else:
        return 0   # 같음
    
def solution(numbers):
    answer = ''
    result = sorted(numbers, key=cmp_to_key(compare))
    answer = ''.join(map(str, result))
    answer = '0' if answer[0] == '0' else answer
    return answer
