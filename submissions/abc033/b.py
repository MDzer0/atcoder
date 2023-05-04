N = int(input())
tLst = [list(map(str, input().split())) for i in range(N)]
ans = 'atcoder'
tmp = 0

for i in range(N):
    tmp += int(tLst[i][1])
ttLst = (sorted(tLst, key=lambda x: int(x[1]), reverse=True))

if (tmp / 2) >= int(ttLst[0][1]):
    print(ans)
else:
    print(ttLst[0][0])
