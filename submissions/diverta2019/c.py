N = int(input())
s = [(input()) for _ in range(N)]

cntA = 0
cntB = 0
cntT = 0
ans = 0
for i in s:
    if i[0] == 'B' and i[-1] == 'A':
        cntT += 1
    else:
        if i[0] == 'B':
            cntB += 1
        if i[-1] == 'A':
            cntA += 1
    ans += i.count('AB')

if cntT > 1:
    ans += cntT - 1
    cntT = 1

if cntA > 0 and cntB > 0 and cntT > 0:
    ans += 2
    cntT -= 1
    cntA -= 1
    cntB -= 1

if cntT > 0:
    if cntA > 0 and cntA >= cntB:
        cntB += 1
    elif cntB > 0:
        cntA += 1

print(ans + min(cntA, cntB))
