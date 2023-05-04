H, W, A, B = map(int, input().split())
hw = [[1] * W for _ in range(H)]
ans = 0

def dfs(x, y, cnt):
    global ans
    if x == H:
        if cnt == A:
            ans += 1
        return

    if y == W:
        dfs(x + 1, 0, cnt)
        return

    if hw[x][y] == 2:
        dfs(x, y + 1, cnt)
        return

    if y < W - 1 and hw[x][y + 1] == 1 and cnt < A:
        hw[x][y + 1] = 2
        dfs(x, y + 1, cnt + 1)
        hw[x][y + 1] = 1

    if x < H - 1 and hw[x + 1][y] == 1 and cnt < A:
        hw[x + 1][y] = 2
        dfs(x, y + 1, cnt + 1)
        hw[x + 1][y] = 1

    dfs(x, y + 1, cnt)
    return

dfs(0, 0, 0)
print(ans)
