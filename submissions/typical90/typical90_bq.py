MOD = 10 ** 9 + 7
N, K = map(int, input().split())
if K <= 2 and N > 2:
    print(0)
    exit()

if N == 1:
    print(K)
    exit()

if N == 2:
    print(K * (K - 1))
    exit()

ans = K * (K - 1)
ans *= pow(K - 2, N - 2, MOD)
print(ans % MOD)
