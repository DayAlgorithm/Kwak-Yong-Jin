def solution(files):
    original = [''] * (len(files))
    changed = []
    for i in range(len(files)):
        original[i] = files[i] # 원래 것들 복사
        
        # head 추출
        head = ''
        tmp_j = 0
        for j in range(len(original[i])):
            if '0' <= original[i][j] <= '9':
                tmp_j = j
                break
            if 'a' <= original[i][j] <= 'z' or 'A' <= original[i][j] <= 'Z':
                head += original[i][j].lower()
            else:
                head += original[i][j]
    
        # number 추출
        number = ''
        last_j = 0
        for j in range(tmp_j, len(original[i])):
            if len(number) > 6:
                last_j = j
                break
            if '0' <= original[i][j] <= '9':
                number += original[i][j]
            else:
                last_j = j
                break
        
        # tail 추출
        tail = original[i][last_j:]
        
        # 합치기
        changed.append((head, int(number), tail, i)) # head, number, tail, idx
    
    changed = sorted(changed, key = lambda x: (x[0], x[1]))
    answer = []
    for i in range(len(changed)):
        _, _, _, idx = changed[i]
        answer.append(original[idx])
    return answer
