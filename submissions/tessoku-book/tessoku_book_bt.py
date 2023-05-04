H, W, K = map(int, input().split())
C = [list(input()) for _ in range(H)]

def paint_row(H, W, d, remaining_steps):
    column = [([d[i][j] for i in range(H)].count('.'), j) for j in range(W)]
    column.sort(reverse=True)

    for i in range(remaining_steps):
        idex = column[i][1]
        for j in range(H):
            d[j][idex] = '#'

    return sum(map(lambda x: x.count('#'), d))

ans = 0
for i in range(1 << H):
    d = [list(C[i]) for i in range(H)]
    remaining_step = K
    for j in range(H):
        if i >> j & 1:
            d[j] = ['#'] * W
            remaining_step -= 1
    if remaining_step >= 0:
        tmp = paint_row(H, W, d, remaining_step)
        ans = max(ans, tmp)

print(ans)
