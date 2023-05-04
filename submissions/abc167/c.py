N, M, X = map(int, input().split())
ca = [list(map(int, input().split())) for _ in range(N)]
ans = 10 ** 18
chk = [0] * N

def dfs(next):
    global ans
    if next == N:
        rikai = [0] * M
        total = 0
        ansF = True
        for i in range(N):
            if chk[i] == 1:
                total += ca[i][0]
                for j in range(M):
                    rikai[j] += ca[i][j + 1]

        for i in rikai:
            if i < X:
                ansF = False
                break
        if ansF:
            ans = min(ans, total)
        return

    for i in range(2):
        chk[next] = i
        dfs(next + 1)
    return

dfs(0)

if ans == 10 ** 18:
    print(-1)
else:
    print(ans)
