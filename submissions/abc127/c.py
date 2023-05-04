N, M = map(int, input().split())
lLst = [0] * M
rLst = [0] * M
for i in range(M):
    lLst[i], rLst[i] = map(int, input().split())

lLst.sort(reverse=True)
rLst.sort()
if lLst[0] > rLst[0]:
    ans = 0
else:
    ans = rLst[0] - lLst[0] + 1

print(ans)
