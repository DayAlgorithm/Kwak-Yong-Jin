def solution(alp, cop, problems):
    end_alp, end_cop = 0, 0
    
    for problem in problems:
        end_alp = max(end_alp, problem[0])
        end_cop = max(end_cop, problem[1])
    
    dp = [[160] * (end_cop+1) for _ in range(end_alp+1)]
    alp = min(alp, end_alp) # 내가 처음에 가지고 있는 알고력이 가장 어려운 문제의 알고력보다 높으면 0을 출력해야 함
    cop = min(cop, end_cop) # 내가 처음에 가지고 있는 코딩력이 가장 어려운 문제의 알고력보다 높으면 0을 출력해야 함
    
    dp[alp][cop] = 0 
    
    for i in range(alp, end_alp+1):
        for j in range(cop, end_cop+1):
            if i < end_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < end_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)
            
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if alp_req <= i and cop_req <= j:
                    new_alp = min(alp_rwd + i, end_alp) # 알고력 경험치랑 원래 내 알고력 더했을 때, 마지막 문제보다 높아지면 마지막 문제에 도달했을 때의 알고력이 이상해짐
                    new_cop = min(cop_rwd + j, end_cop) # 코딩력 경험치랑 원래 내 코딩력 더했을 때, 마지막 문제보다 높아지면 마지막 문제에 도달했을 때의 코딩력이 이상해짐
                    dp[new_alp][new_cop] = min(dp[new_alp][new_cop], dp[i][j] + cost)
                    
    return dp[end_alp][end_cop]
