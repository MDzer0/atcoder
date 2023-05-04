N = int(input())
S = [list(input()) for _ in range(N)]

ans = 0
cntM = 0
cntA = 0
cntR = 0
cntC = 0
cntH = 0
for i in range(N):
    cntM += (1 if S[i][0] == 'M' else 0)
    cntA += (1 if S[i][0] == 'A' else 0)
    cntR += (1 if S[i][0] == 'R' else 0)
    cntC += (1 if S[i][0] == 'C' else 0)
    cntH += (1 if S[i][0] == 'H' else 0)
cntlst = [cntM, cntA, cntR, cntC, cntH]

for i in range(3):
    for j in range(i + 1, 4):
        for k in range(j + 1, 5):
            ans += cntlst[i] * cntlst[j] * cntlst[k]
print(ans)
