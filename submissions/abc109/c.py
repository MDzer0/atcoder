from fractions import gcd

N, X = map(int, input().split())
x = list(map(int, input().split()))

tmp = [0] * N
x.sort()
tmp[0] = abs(X - x[0])

for i in range(N - 1):
    tmp[i + 1] = x[i + 1] - x[i]

ans = 0
for i in range(N):
    ans = gcd(ans, tmp[i])

print(ans)
