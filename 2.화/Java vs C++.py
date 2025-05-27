import sys
input = sys.stdin.readline

def java_to_cpp(s):
    result = ''
    for num in s:
        if 'a' <= num <= 'z':
            result += num
            continue
        elif 'A' <= num <= 'Z':
            num = chr(ord(num) + 32)
            result += '_' + num
    
    return result

def cpp_to_java(s):
    result = ''
    prevunder = False
    for num in s:
        if 'a' <= num <= 'z':
            if prevunder:
                num = chr(ord(num) - 32)
                prevunder = False
            result += num
            continue
        elif num == '_':
            if prevunder:   # _가 연속으로 나오면 에러
                print("Error!")
                exit()
            prevunder = True

    return result

s = input().rstrip()

if s[0] == '_' or s[-1] == '_' or 'A' <= s[0] <= 'Z': # 예외처리, 처음이 _이거나 마지막이 _이거나 처음이 대문자면 에러
    print("Error!")
    exit()

# 유형체크
all_small = True
big = False
under = False
error = False
for num in s:
    if 'a' <= num <= 'z':
        continue
    
    elif 'A' <= num <= 'Z':
        all_small = False
        big = True

        if under:
            error = True
            print("Error!")
            exit()
        
    elif num == '_':
        all_small = False
        under = True

        if big:
            error = True
            print("Error!")
            exit()

if all_small:
    print(s)
    exit()

if big and not under:
    print(java_to_cpp(s))

if not big and under:
    print(cpp_to_java(s))
