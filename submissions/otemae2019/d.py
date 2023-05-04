N, M = map(int, input().split())
S = [input() for _ in range(M)]
dp =[[[0] * 3 for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][0][0] = 1
MOD = 10 ** 9 + 7

for i in range(N):
    for j in range(M + 1):
        for k in range(3):
            cnt = 0
            if i == 0:
                cnt = 1
            for l in range(cnt, 10):
                f = (k + l) % 3 == 0
                b = l % 5 == 0
                if (f or b) and j == M:
                    continue
                if (f and b and S[j] == 'FizzBuzz') or \
                        (f and (not b) and S[j] == 'Fizz') or \
                        ((not f) and b and S[j] == 'Buzz'):
                    dp[i + 1][j + 1][(k + l) % 3] += dp[i][j][k]
                    dp[i + 1][j + 1][(k + l) % 3] %= MOD
                elif not f and not b:
                    dp[i + 1][j][(k + l) % 3] += dp[i][j][k]
                    dp[i + 1][j][(k + l) % 3] %= MOD

ans = 0
for i in range(3):
    ans += dp[N][M][i]
    ans %= MOD

print(ans)
