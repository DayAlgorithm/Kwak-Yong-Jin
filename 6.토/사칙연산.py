def solution(arr):
    nums = []
    ops = []
    for i in range(len(arr)):
        if i % 2 == 0:
            nums.append(int(arr[i]))
        else:
            ops.append(arr[i])

    n = len(nums)
    dp_max = [[float('-inf')] * n for _ in range(n)]
    dp_min = [[float('inf')] * n for _ in range(n)]

    for i in range(n):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]

    for length in range(1, n):
        for i in range(n - length):
            j = i + length
            
            for k in range(i, j):
                op = ops[k]
                if op == '+':
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] + dp_max[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] + dp_min[k+1][j])
                else: 
                    dp_max[i][j] = max(dp_max[i][j], dp_max[i][k] - dp_min[k+1][j])
                    dp_min[i][j] = min(dp_min[i][j], dp_min[i][k] - dp_max[k+1][j])

    return dp_max[0][n-1]
