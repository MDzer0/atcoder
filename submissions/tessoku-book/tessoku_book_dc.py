MOD = 10 ** 9 + 7
H, W = map(int, input().split())

a = 1
for i in range(1, H + W - 1):
    a *= i
    a %= MOD

b = 1
for i in range(1, min(H, W)):
    b *= i
    b %= MOD

for i in range(1, max(H, W)):
    b *= i
    b %= MOD

print((a * pow(b, MOD - 2, MOD)) % MOD)
