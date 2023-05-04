N = int(input())
aLst = list(map(int, input().split()))
bLst = list(map(int, input().split()))

ans = 0

for i in range(N):
    tmp = aLst[i] - bLst[i]
    if tmp < 0:
        if aLst[i + 1] - (bLst[i] - aLst[i]) <= 0:
            ans += aLst[i] + aLst[i + 1]
            aLst[i + 1] = 0
        else:
            ans += bLst[i]
            aLst[i + 1] = aLst[i + 1] - (bLst[i] - aLst[i])
    else:
        ans += bLst[i]
print(ans)
