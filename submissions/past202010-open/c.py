N, M = map(int, input().split())
s = [list(input()) for _ in range(N)]
ans = [[0] * M for _ in range(N)]
x = [1, 1, 1, 0, 0, 0, -1, -1, -1]
y = [1, -1, 0, 1, -1, 0, 1, -1, 0]

for i in range(N):
    for j in range(M):
        cnt = 0
        for k in range(len(x)):
            if i + x[k] >= 0 and i + x[k] < N\
                and j + y[k] >= 0 and j + y[k] < M:
                if s[i + x[k]][j + y[k]] == '#':
                    cnt += 1
        ans[i][j] = cnt

for i in ans:
    print(*i, sep='')
