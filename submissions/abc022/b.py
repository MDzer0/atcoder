N = int(input())
aLst = list(int(input()) for i in range(N))
ans = 0
cntLst = [0] * (10 ** 5)
for i in range(N):
    if cntLst[aLst[i] - 1] != 0:
        cntLst[aLst[i] - 1] += 1
        ans += 1
    else:
        cntLst[aLst[i] - 1] += 1
print(ans)
