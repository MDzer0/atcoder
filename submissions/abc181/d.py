S = input()
yakusu = []
ketaCnt = [0] * 10

for i in S:
    ketaCnt[int(i)] += 1

for i in range(100, 1000):
    if i % 8 == 0:
        yakusu.append(i)

if len(S) >= 3:
    for i in yakusu:
        ansF = True
        hikakuCnt = [0] * 10
        tmp = str(i)
        for j in tmp:
            hikakuCnt[int(j)] += 1
        for j in range(10):
            if ketaCnt[j] >= hikakuCnt[j]:
                continue
            else:
                ansF = False
                break
        if ansF:
            print('Yes')
            exit()
    print('No')

else:
    if int(S) % 8 == 0:
        print('Yes')
    elif int(S[::-1]) % 8 == 0:
        print('Yes')
    else:
        print('No')
