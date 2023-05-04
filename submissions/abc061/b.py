N, M = map(int, input().split())

aLst = [0] * M
bLst = [0] * M

for i in range(M):
    a, b = map(int, input().split())
    aLst[i] = a
    bLst[i] = b

for i in range(1, N + 1):
    ans = aLst.count(i)
    ans += bLst.count(i)
    print(ans)
