N, M = map(int, input().split())
b = [list(map(int, input())) for _ in range(N)]
ans = [[0] * M for _ in range(N)]

for i in range(1, N - 1):
    for j in range(1, M - 1):
        mintmp = min(b[i - 1][j], b[i + 1][j], b[i][j - 1], b[i][j + 1])
        if mintmp == 0:
            continue
        ans[i][j] += mintmp
        b[i - 1][j] -= mintmp
        b[i + 1][j] -= mintmp
        b[i][j - 1] -= mintmp
        b[i][j + 1] -= mintmp

for i in ans:
    print(*i, sep='')
