H, W = map(int, input().split())
s = [input() for _ in range(H)]

ocnt = [[0 for _ in range(W)] for _ in range(H)]
icnt = [[0 for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if s[i][j] == 'O':
            if j != 0:
                ocnt[i][j] = ocnt[i][j - 1] + 1
        else:
            if j != 0:
                ocnt[i][j] = ocnt[i][j - 1]
        if s[i][j] == 'I':
            if i != 0:
                icnt[i][j] = icnt[i - 1][j] + 1
        else:
            if i != 0:
                icnt[i][j] = icnt[i - 1][j]


ans = 0
for i in range(H):
    for j in range(W):
        if s[i][j] == 'J':
            ans += (ocnt[i][-1] - ocnt[i][j]) * (icnt[-1][j] - icnt[i][j])

print(ans)
