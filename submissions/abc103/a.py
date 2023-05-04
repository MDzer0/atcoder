ALst = list(map(int, input().split()))

tLst = []
for i in range(3):
    for j in range(i, 2):
        tLst.append(int(abs(ALst[i] - ALst[j + 1])))

tLst.sort()
ans = tLst[0] + tLst[1]
print(ans)
