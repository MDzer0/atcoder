MOD = 10 ** 9 + 7
n, r = map(int, input().split())

a = 1
for i in range(1, n + 1):
    a *= i
    a %= MOD

b = 1
for i in range(1, r + 1):
    b *= i
    b %= MOD

for i in range(1, n - r + 1):
    b *= i
    b %= MOD

print((a * pow(b, MOD - 2, MOD)) % MOD)
