class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        m = len(matrix)
        n = len(matrix[0])
        chk = set()
        cur_x, cur_y = 0, 0
        flag = 1 # 1: 오른쪽, 2: 아래쪽, 3, 왼쪽, 4: 위쪽
        while len(answer) != (m * n):
            answer.append(matrix[cur_x][cur_y])
            chk.add((cur_x, cur_y))
            if flag == 1:
                cur_y += 1
                if cur_y == n - 1:
                    flag = 2
                
                if cur_y > n - 1:
                    cur_y -= 1
                    flag = 2
                
                if (cur_x, cur_y) in chk:
                    cur_y -= 1
                    cur_x += 1
                    flag = 2
                continue
            
            if flag == 2:
                cur_x += 1
                if cur_x == m - 1:
                    flag = 3
                
                if cur_x > m - 1:
                    cur_x -= 1
                    flag = 3
                
                if (cur_x, cur_y) in chk:
                    cur_x -= 1
                    cur_y -= 1
                    flag = 3
                continue

            if flag == 3:
                cur_y -= 1       
                if cur_y == 0:
                    flag = 4
                
                if cur_y < 0:
                    cur_y += 1
                    flag = 4
                
                if (cur_x, cur_y) in chk:
                    cur_y += 1
                    cur_x -= 1
                    flag = 4
                continue

            if flag == 4:
                cur_x -= 1
                if cur_x == 0:
                    flag = 1
                
                if cur_x < 0:
                    cur_x += 1
                    flag = 1
                
                if (cur_x, cur_y) in chk:
                    cur_x += 1
                    cur_y += 1
                    flag = 1
        return answer
