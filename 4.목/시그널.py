import sys
input = sys.stdin.readline

# 패턴 정의
patterns = {
    '0': ['###', '#.#', '#.#', '#.#', '###'],
    '1': ['#', '#', '#', '#', '#'],
    '2': ['###', '..#', '###', '#..', '###'],
    '3': ['###', '..#', '###', '..#', '###'],
    '4': ['#.#', '#.#', '###', '..#', '..#'],
    '5': ['###', '#..', '###', '..#', '###'],
    '6': ['###', '#..', '###', '#.#', '###'],
    '7': ['###', '..#', '..#', '..#', '..#'],
    '8': ['###', '#.#', '###', '#.#', '###'],
    '9': ['###', '#.#', '###', '..#', '###']
}

n = int(input())
s = input().rstrip()

# 입력 정리
length = n // 5
signal = [s[i:i+length] for i in range(0, n, length)]

result = ""
i = 0

while i < length:
    # 싹 다 .이면 다음차례로
    if all(signal[j][i] == '.' for j in range(5)):
        i += 1
        continue
    # 만약 #인 부분의 열은 전부 #이고 그 다음 열이 다 . 이면 무조건 1임
    if i + 1 < length and all(signal[j][i] == '#' for j in range(5)) and all(signal[j][i+1] == '.' for j in range(5)):
        result += '1'
        i += 2
        continue
      
    if i + 2 < length:
        pattern = []
        for j in range(5):
            pattern.append(signal[j][i:i+3])
        
        for digit, digit_pattern in patterns.items():
            if pattern == digit_pattern:
                result += digit
                # 숫자 넓이 3칸과 그 다음 공백 1칸
                i += 4
                break
        else: # 아무것도 안맞으면 숫자 1 (for 문에 걸린 else임)
            result += '1'
            i += 2
    else: # 만약 남아 있는 칸이 자기 앞 2칸이 안되면 1밖에 안됨
        result += '1'
        i += 2

print(result)
