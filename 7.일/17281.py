import sys
import itertools
input = sys.stdin.readline

def solve():
    n = int(input())
    rounds = [list(map(int, input().split())) for _ in range(n)]

    others = [i for i in range(1, 9)]
    max_score = 0

    for p in itertools.permutations(others):
        p = list(p)
        batting_order = p[:3] + [0] + p[3:]
        
        score = 0
        idx = 0  
        
        for inning_results in rounds:
            out = 0
            b1, b2, b3 = 0, 0, 0 
            
            while out < 3:
                res = inning_results[batting_order[idx]]
                if res == 0:
                    out += 1
                elif res == 1:
                    score += b3
                    b1, b2, b3 = 1, b1, b2
                elif res == 2: 
                    score += (b2 + b3)
                    b1, b2, b3 = 0, 1, b1
                elif res == 3: 
                    score += (b1 + b2 + b3)
                    b1, b2, b3 = 0, 0, 1
                elif res == 4: 
                    score += (b1 + b2 + b3 + 1)
                    b1, b2, b3 = 0, 0, 0
                
                idx = (idx + 1) % 9
        
        if score > max_score:
            max_score = score
            
    print(max_score)

solve()
