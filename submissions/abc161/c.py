N, K = map(int, input().split())
if N == K:
    print(0)
    exit()

tmp1 = 0
if N > K:
    tmp, m = divmod(N, K)
    tmp1 = m
    tmp1 = min(tmp1, abs(m - K))
else:
    tmp = abs(N - K)
    tmp1 = min(N % K, tmp)

print(tmp1)
