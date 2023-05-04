import sys

A, B, C = map(int, input().split())
aLst = [A]
bLst = [B]
cLst = [C]
cnt = 0
if A % 2 == 1 or B % 2 == 1 or C % 2 == 1:
    print(0)
    sys.exit()
    
for i in range(1000000000000):
    atmp = (bLst[i] // 2) + (cLst[i] // 2)
    btmp = (aLst[i] // 2) + (cLst[i] // 2)
    ctmp = (aLst[i] // 2) + (bLst[i] // 2)
    aLst.append(atmp)
    bLst.append(btmp)
    cLst.append(ctmp)
    if atmp % 2 == 1 or btmp % 2 == 1 or ctmp % 2 == 1:
        cnt += 1
        break
    elif atmp == btmp and btmp == ctmp and atmp == ctmp:
        cnt = -1
        break
    else:
        cnt += 1

print(cnt)
