MOD = 10 ** 9 + 7

N = int(input())
Alist = []
for i in range(N):
    a = list(map(int, input().split()))
    Alist.append(a)

dp = [[0] * (1 << N) for _ in range(N + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(1 << N):
        if dp[i][j]:
            for k in range(N):
                if Alist[i][k] == 1 and (j >> k) & 1 == 0:
                    dp[i + 1][j | 1 << k] += dp[i][j]
                    dp[i + 1][j | 1 << k] %= MOD
print(dp[N][-1])
