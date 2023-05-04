MOD = 998244353
a, b, c = map(int, input().split())
asum = (((a + 1) * a) // 2) % MOD
bsum = (((b + 1) * b) // 2) % MOD
csum = (((c + 1) * c) // 2) % MOD

ans = (asum * bsum) % MOD
ans = (ans * csum) % MOD
print(ans)
