from fractions import gcd
N, K = map(int, input().split())
a = list(map(int, input().split()))
g = 0

for i in range(N):
    g = gcd(a[i], g)
amax = max(a)
q, mod = divmod(K, g)

if mod != 0 or amax < K:
    print('IMPOSSIBLE')
else:
    print('POSSIBLE')
