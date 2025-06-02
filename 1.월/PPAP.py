import sys
input = sys.stdin.readline

s = list(input().rstrip())
check = []

while s:
    tmp = s.pop()
    
    check.append(tmp)

    if len(check) < 4:
        continue

    while len(check) >= 4:
        if check[-4:] == ["P","A","P","P"]:
            check.pop()
            check.pop()
            check.pop()
            check.pop()
            check.append("P")
        else:
            break
    
if check == ["P"]: # 맨 마지막에 PPAP는 P가 되니까
    print("PPAP")
else:
    print("NP")
