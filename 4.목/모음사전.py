alpha = ['A', 'E', 'I', 'O', 'U']
target = ""
answer = 0
cnt = 0
found = False

def dfs(cur):
    global cnt, answer, found
    if found:   # 이미 찾았으면 더 안 봐도 됨
        return
    if cur:     # 공백("")은 제외
        cnt += 1
        if cur == target:
            answer = cnt
            found = True
            return
    
    if len(cur) == 5:  # 단어 길이 제한
        return
    
    for ch in alpha:
        dfs(cur + ch)

def solution(word):
    global target, answer, cnt, found
    target = word
    answer, cnt, found = 0, 0, False
    dfs("")
    return answer
