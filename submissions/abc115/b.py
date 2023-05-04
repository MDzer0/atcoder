N = int(input())
pLst = [0] * N
for i in range(N):
    pLst[i] = int(input())

ans = 0
pLst.sort(reverse=True)
for i in range(1, N):
    ans += pLst[i]

ans += int(pLst[0] / 2)
print(ans)
