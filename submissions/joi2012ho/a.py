S = input()
ans = 0
index = 0
jCnt = 0
oCnt = 0
iCnt = 0
for i in S:
    if index == 0:
        if i == 'J':
            jCnt += 1
            continue
        else:
            if jCnt != 0:
                index += 1
            else:
                jCnt, oCnt, iCnt = 0, 0, 0
                index = 0
                continue

    if index == 1:
        if i == 'O':
            oCnt += 1
            continue
        else:
            if oCnt != 0:
                index += 1
            else:
                jCnt, oCnt, iCnt = 0, 0, 0
                if i == 'J':
                    jCnt += 1
                index = 0
                continue

    if index == 2:
        if i == 'I':
            iCnt += 1
            continue
        else:
            if iCnt != 0:
                index += 1
            else:
                jCnt, oCnt, iCnt = 0, 0, 0
                if i == 'J':
                    jCnt += 1
                index = 0
                continue

    if index == 3:
        index = 0
        if jCnt >= oCnt and oCnt <= iCnt:
            ans = max(ans, min(jCnt, oCnt, iCnt))
        jCnt, oCnt, iCnt = 0, 0, 0
        if i == 'J':
            jCnt += 1
if index == 2:
    if jCnt >= oCnt and oCnt <= iCnt:
        ans = max(ans, min(jCnt, oCnt, iCnt))

print(ans)
