inLst = [0] * 3
for i in range(3):
    inLst[i] = int(input())

ans = inLst[0] - inLst[1]
ans = ans % inLst[2]
print(ans)
