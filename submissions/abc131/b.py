N, L = map(int, input().split())
tmp = L
total = 0
aLst = [0] * N
for i in range(N):
    aLst[i] = tmp + i
    total += aLst[i]

ansL = [0] * N
ansM = [0] * N
for i in range(N):
    tmp = 0
    for j in range(N):
        if i == j:
            continue
        tmp += aLst[j]
    ansL[i] = tmp
    ansM[i] = abs(total - tmp)

ans = ansL[0]
tmp = ansM[0]
for i in range(1, N):
    if tmp > ansM[i]:
        tmp = ansM[i]
        ans = ansL[i]


print(ans)
