N = int(input())
W = list(input() for _ in range(N))
wordlst = [''] * N
ans = 'DRAW'
wordlst[0] = W[0]
for i in range(1, N):
    if wordlst.count(W[i]) > 0:
        if i % 2 != 1:
            ans = 'LOSE'
            break
        else:
            ans = 'WIN'
            break

    if W[i - 1][-1] != W[i][0]:
        if i % 2 != 1:
            ans = 'LOSE'
            break
        else:
            ans = 'WIN'
            break
    wordlst[i] = W[i]

print(ans)
