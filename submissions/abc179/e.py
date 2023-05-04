N, X, M = map(int, input().split())
total = [X]
ans = X
index = 0
loopF = False
chklst = [-1] * (M + 1)
chklst[X] = 0
for i in range(1, N):
    tmp = total[i - 1] ** 2 % M
    if chklst[tmp] != -1:
        index = chklst[tmp]
        loopF = True
        break
    else:
        ans += tmp
        chklst[tmp] = i
    total.append(tmp)
if loopF:
    totallen = len(total) - index
    N -= len(total)
    m, d = divmod(N, totallen)
    ans += sum(total[index:]) * m + sum(total[index:d + index])

print(ans)
