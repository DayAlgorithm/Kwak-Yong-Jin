def solution(tickets):
    tickets.sort()  # 사전순 정렬
    used = [False] * len(tickets)
    path = ["ICN"]
    n = len(tickets)
    answer = []

    def dfs(cur, count):
        if count == n:
            answer.extend(path)
            return True  # 경로 완성

        for i in range(n):
            if not used[i] and tickets[i][0] == cur:
                used[i] = True
                path.append(tickets[i][1])

                if dfs(tickets[i][1], count + 1):
                    return True

                path.pop()
                used[i] = False

        return False

    dfs("ICN", 0)
    return answer
