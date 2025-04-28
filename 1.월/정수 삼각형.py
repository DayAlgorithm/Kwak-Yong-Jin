def solution(triangle):
    for i in range(0, len(triangle)-1):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i+1][j] += triangle[i][j] # 삼각형 맨 왼쪽은 비교할 필요 없음
            if j == len(triangle[i]) - 1:
                triangle[i+1][j+1] += triangle[i][j] # 삼각형 맨 오른쪽도 비교할 필요가 없음
                continue
            tmp = max(triangle[i][j], triangle[i][j+1]) # 양쪽에서 더 큰 것을 들고오기
            triangle[i+1][j+1] = tmp + triangle[i+1][j+1]
    answer = max(triangle[len(triangle)-1]) # 맨 마지막에서 제일 큰 값 추출
    return answer
