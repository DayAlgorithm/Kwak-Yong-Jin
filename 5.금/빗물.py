import sys
input = sys.stdin.readline

h, w = map(int, input().split())
graph = list(map(int, input().split()))
height = max(graph)
cnt = 0
for i in range(height + 1):
    for j in range(w):
        if graph[j] <= i:
            flag_left = False
            flag_right = False

            for k in range(j - 1, -1, -1):
                if graph[k] > i:
                    flag_left = True
                    break
            
            for k in range(j + 1, w):
                if graph[k] > i:
                    flag_right = True
                    break   

            if flag_left and flag_right:
                cnt += 1
print(cnt)
