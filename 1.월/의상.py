from collections import defaultdict

def solution(clothes):
    cloth_dic = defaultdict(int)
    for _, cloth_type in clothes:
        cloth_dic[cloth_type] += 1
    
    answer = 1
    for count in cloth_dic.values():
        answer *= (count + 1)

    return answer - 1
