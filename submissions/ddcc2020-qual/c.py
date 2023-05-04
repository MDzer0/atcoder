H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]

index = 0
for i in range(H):
    cnt = 0
    for j in range(W):
        if c[i][j] == '#':
            index += 1
            cnt = index
            c[i][j] = cnt
        if c[i][j] == '.' and cnt != 0:
            c[i][j] = cnt

for i in range(H):
    for j in reversed(range(W - 1)):
        if c[i][j] == '.':
            c[i][j] = c[i][j + 1]

for i in range(H - 1):
    for j in range(W):
        if c[i][j] != '.' and c[i + 1][j] == '.':
            c[i + 1][j] = c[i][j]

for i in reversed(range(1, H)):
    for j in range(W):
        if c[i][j] != '.' and c[i - 1][j] == '.':
            c[i - 1][j] = c[i][j]


for i in range(H):
    for j in range(W):
        if j != W - 1:
            print(c[i][j], end=' ')
        else:
            print(c[i][j])
