def solution(distance, rocks, n):
    rocks.sort()
    low, high = 1, distance  # 가능한 최소 거리와 최대 거리를 범위로 설정
    answer = 0

    while low <= high:
        mid = (low + high) // 2
        remove_count = 0
        prev = 0  # 출발점

        for rock in rocks:
            if rock - prev < mid:
                remove_count += 1  # mid보다 거리 짧으면 제거
            else:
                prev = rock

        # 마지막 구간: 마지막 바위부터 도착점까지의 거리
        if distance - prev < mid:
            remove_count += 1

        if remove_count > n:  # 제거한 돌이 n보다 많으면 mid가 너무 큼
            high = mid - 1
        else:  # n 이하로 제거 가능하다면 mid가 유효한 값
            answer = mid
            low = mid + 1

    return answer
