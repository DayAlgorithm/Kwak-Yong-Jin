import sys
input = sys.stdin.readline

signal = input().strip()
duck = []
cnt = 0
for i in range(len(signal)):
    if cnt == 0:
        if signal[i] == 'q':
            cnt += 1
            duck.append("q")
        else:
            print(-1)
            sys.exit()
    
    else:
        flag1 = False
        if signal[i] == 'q':
            flag2 = False
            for j in range(len(duck)):
                if duck[j] == "":
                    duck[j] += 'q'
                    flag2 = True
                    break
            
            if flag2 == False:
                cnt += 1
                duck.append("q")
            
            flag1 = True

        elif signal[i] == 'u':
            for j in range(len(duck)):
                if duck[j] == "":
                    continue
                if duck[j][-1] == 'q':
                    duck[j] += 'u'
                    flag1 = True
                    break

        elif signal[i] == 'a':
            for j in range(len(duck)):
                if duck[j] == "":
                    continue
                if duck[j][-1] == 'u':
                    duck[j] += 'a'
                    flag1 = True
                    break
                
        elif signal[i] == 'c':
            for j in range(len(duck)):
                if duck[j] == "":
                    continue
                if duck[j][-1] == 'a':
                    duck[j] += 'c'
                    flag1 = True
                    break

        elif signal[i] == 'k':
            for j in range(len(duck)):
                if duck[j] == "":
                    continue
                if duck[j][-1] == 'c':
                    duck[j] += 'k'
                    flag1 = True

                    if duck[j] == 'quack':
                        duck[j] = ""
                    break
        
        if flag1 == False:
            print(-1)
            sys.exit()

flag3 = True
for i in range(len(duck)):
    if duck[i] != "":
        flag3 = False
        break
if flag3 == False:
    print(-1)
else:
    print(cnt)
