sList = list(map(int, input().split()))
cnt5 = 0
cnt7 = 0
ansFlg = True
for i in sList:
    if i == 5:
        if cnt5 == 3:
            ansFlg = False
            break
        cnt5 += 1
        continue
    elif i == 7:
        cnt7 += 1
        if cnt7 == 2:
            ansFlg = False
            break
        continue
    else:
        ansFlg = False
        break
if ansFlg:
    print('YES')
else:
    print('NO')
