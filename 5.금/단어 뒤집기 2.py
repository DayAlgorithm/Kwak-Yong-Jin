import sys
input = sys.stdin.readline

s = input().rstrip()
result = ''

flag = False
tmp = ''
for i in range(len(s)):
    if s[i] == '<':
        if tmp:
            tmp = tmp[::-1]
            result += tmp
            tmp = ''
        flag = True
        result += s[i]
        continue

    elif s[i] == '>':
        flag = False
        result += s[i]
        continue

    elif s[i] == ' ':
        if flag == False:
            tmp = tmp[::-1]
            result += tmp
            result += ' '
            tmp = ''
        
        else:
            result += ' '
    
    else:
        if flag:
            result += s[i]
        
        else:
            tmp += s[i]
    
if tmp:
    tmp = tmp[::-1]
    result += tmp
print(result)
