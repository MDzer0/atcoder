INF = 10 ** 18

def data3():
    dp = [[INF] * (10 ** 5 + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    for i in range(N):
        for j in range(10 ** 5 + 1):
            if dp[i][j] == INF: continue
            if dp[i][j] + vw[i][0] <= W:
                dp[i + 1][j + vw[i][1]] = min(dp[i][j + vw[i][1]], dp[i][j] + vw[i][0])
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
    ans = 0
    for i in range(10 ** 5 + 1):
        if dp[N][i] != INF:
            ans = i
    print(ans)
    exit()

N, W = map(int, input().split())
vw = [list(map(int, input().split())) for _ in range(N)]
data3()
