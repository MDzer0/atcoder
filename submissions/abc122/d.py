MOD = 10 ** 9 + 7
N = int(input())

dp = [[[[0] * 5 for _ in range(5)] for _ in range(5)] for _ in range(N + 1)]
dp[0][0][0][0] = 1

# AGC, GAC, ACG, A*GC, AG*C èúäO
for i in range(N):
    for j in range(5):
        for k in range(5):
            for l in range(5):
                for m in range(1, 5):
                    if k == 1 and l == 2 and m == 3: continue
                    if k == 2 and l == 1 and m == 3: continue
                    if k == 1 and l == 3 and m == 2: continue
                    if j == 1 and l == 2 and m == 3: continue
                    if j == 1 and k == 2 and m == 3: continue
                    dp[i + 1][k][l][m] += dp[i][j][k][l]
                    dp[i + 1][k][l][m] %= MOD

ans = 0
for i in range(5):
    for j in range(5):
        for k in range(5):
            ans += dp[N][i][j][k]
            ans %= MOD
print(ans)
