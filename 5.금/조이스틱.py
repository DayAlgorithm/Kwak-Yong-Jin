def solution(name):
    answer = 0
    cnt = [0] * (len(name))
    for i in range(len(name)):
        cnt[i] = min(ord(name[i]) - ord('A'), ord('Z') - ord(name[i]) + 1)
        
    answer += sum(cnt)      
    
    move = len(name) - 1
    for i in range(len(name)):
        nxt = i + 1
        while nxt < len(name) and name[nxt] == 'A':
            nxt += 1
        move = min(move, 2 * i + len(name) - nxt, i + 2 * (len(name) - nxt))

    answer += move
    return answer
