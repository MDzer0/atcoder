SIRO = '.'
KURO = '#'
N = int(input())
S = input()
sCnt = S.count(SIRO)
kCnt = 0
ans = sCnt
for i in S:
    if i == KURO:
        kCnt += 1
    else:
        sCnt -= 1
    ans = min(ans, kCnt + sCnt)

print(ans)
