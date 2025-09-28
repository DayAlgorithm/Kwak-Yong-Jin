def solution(str1, str2):
    # 특수 기호나 공백 없애기 + 대문자면 소문자로 바꾸기
    new_str1 = ''
    for i in range(len(str1)):
        if 'A' <= str1[i] <= 'Z': 
            new_str1 += chr(ord(str1[i]) + 32)
        elif 'a' <= str1[i] <= 'z':
            new_str1 += str1[i]
        else:
            new_str1 += ' '
            
    new_str2 = ''
    for i in range(len(str2)):
        if 'A' <= str2[i] <= 'Z': 
            new_str2 += chr(ord(str2[i]) + 32)
        elif 'a' <= str2[i] <= 'z':
            new_str2 += str2[i]
        else:
            new_str2 += ' '
            
    # 두 글자 다중집합 원소 만들기
    new_set1 = dict()
    for i in range(len(new_str1) - 1):
        if new_str1[i] == ' ' or new_str1[i+1] == ' ':
            continue
        tmp = new_str1[i] + new_str1[i+1]
        if tmp in new_set1:
            new_set1[tmp] += 1
        else:
            new_set1[tmp] = 1
    
    new_set2 = dict()
    for i in range(len(new_str2) - 1):
        if new_str2[i] == ' ' or new_str2[i+1] == ' ':
            continue
        tmp = new_str2[i] + new_str2[i+1]
        if tmp in new_set2:
            new_set2[tmp] += 1
        else:
            new_set2[tmp] = 1
    
    # 계산하기
    union = 0
    intersection = 0
    for key, value in new_set1.items():
        if not key in new_set2:
            union += value
        else:
            union += max(value, new_set2[key])
            intersection += min(value, new_set2[key])
    
    for key, value in new_set2.items():
        if not key in new_set1:
            union += value
    
    if union == 0:
        answer = 65536
    else:
        answer = int((intersection/union) * 65536) 
    return answer
