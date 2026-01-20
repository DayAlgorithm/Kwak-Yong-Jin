class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = [[] for _ in range(numRows)]
        a_idx = 0
        a_flag = True

        s_idx = 0
        while s_idx < len(s):
            answer[a_idx].append(s[s_idx])
            s_idx += 1

            if numRows == 1:
                continue
            
            if a_idx == numRows - 1:
                a_flag = False
            
            if a_idx == 0:
                a_flag = True
            
            if a_flag:
                a_idx += 1
            else:
                a_idx -= 1
        
        tmp = ''
        for i in range(len(answer)):
            tmp += ''.join(answer[i])
        
        return tmp
