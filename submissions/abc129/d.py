H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]
l = [[0] * W for _ in range(H)]
r = [[0] * W for _ in range(H)]
u = [[0] * W for _ in range(H)]
d = [[0] * W for _ in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] != '#':
            if j != 0:
                r[i][j] = r[i][j - 1] + 1
            else:
                r[i][j] = 1

for i in range(H):
    for j in reversed(range(W)):
        if S[i][j] != '#':
            if j != W - 1:
                l[i][j] = l[i][j + 1] + 1
            else:
                l[i][j] = 1

for i in range(W):
    for j in range(H):
        if S[j][i] != '#':
            if j != 0:
                d[j][i] = d[j - 1][i] + 1
            else:
                d[j][i] = 1

for i in range(W):
    for j in reversed(range(H)):
        if S[j][i] != '#':
            if j != H - 1:
                u[j][i] = u[j + 1][i] + 1
            else:
                u[j][i] = 1

for i in range(H):
    for j in range(W):
        tmp = l[i][j] + r[i][j] + u[i][j] + d[i][j] - 3
        ans = max(ans, tmp)

print(ans)
