cnt = 0 # cnt 전역변수

def dfs(depth, cur, target, numbers): # 백트래킹
    global cnt
    if depth == (len(numbers) - 1):
        if cur == target:
            cnt += 1 # 결과값
            return
        return
        
    dfs(depth+1, cur + numbers[depth+1], target, numbers) # 하나는 더하기
    dfs(depth+1, cur - numbers[depth+1], target, numbers) # 하나는 뺴기
    
def solution(numbers, target):
    global cnt
    dfs(0, numbers[0], target, numbers) # 처음 수를 +로
    dfs(0, -numbers[0], target, numbers) # 처음 수를 -로
    answer = cnt
    return answer
