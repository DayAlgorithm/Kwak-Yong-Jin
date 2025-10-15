from collections import defaultdict

def solution(survey, choices):
    answer = ''
    score = defaultdict(int)
    for i in range(len(survey)):
        a, b = survey[i][0], survey[i][1]
        if choices[i] == 1:
            score[a] += 3
        if choices[i] == 2:
            score[a] += 2
        if choices[i] == 3:
            score[a] += 1
        
        if choices[i] == 5:
            score[b] += 1
        if choices[i] == 6:
            score[b] += 2
        if choices[i] == 7:
            score[b] += 3
    
    if score['R'] >= score['T']:
        answer += 'R'
    else:
        answer += 'T'
    
    if score['C'] >= score['F']:
        answer += 'C'
    else:
        answer += 'F'
    
    if score['J'] >= score['M']:
        answer += 'J'
    else:
        answer += 'M'
    
    if score['A'] >= score['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer
