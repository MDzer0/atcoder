import itertools

N = int(input())
C = list(input())

shtcmd = []
for i, j in itertools.product(('A', 'B', 'X', 'Y'), repeat=2):
    shtcmd.append(i+j)

ans = 10**9
for l, r in itertools.combinations(shtcmd, 2):
    dp = [10**9 for i in range(N + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = min(dp[i], dp[i - 1] + 1)
        if C[i - 2]+C[i - 1] == l or C[i - 2]+C[i - 1] == r:
            dp[i] = min(dp[i - 2] + 1, dp[i])


    ans = min(ans, dp[N])

print(ans)
