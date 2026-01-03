import sys
input = sys.stdin.readline

n = int(input())
trans = dict() 
graph = []
num = []
for i in range(n):
    word = input().strip()
    for j in range(len(word)):
        weight = 10 ** (len(word) - j - 1)
        if word[j] in trans:
            trans[word[j]] += weight
        else:
            trans[word[j]] = weight
trans = list(trans.items())
trans = sorted(trans, key=lambda x:-x[1])
answer = 0
for i in range(len(trans)):
    answer += (trans[i][1] * (9-i))
print(answer)
