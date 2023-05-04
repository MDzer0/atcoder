MOD = 10 ** 9 + 7
N, K = map(int, input().split())
ruiMin = [0] * (N + 1)
ruiMax = [((N + 1) * N) // 2] * (N + 1)

for i in range(1, N + 1):
    ruiMin[i] = ruiMin[i - 1] + i

for i in range(1, N + 1):
    ruiMax[-i - 1] = ruiMax[-i] - (i - 1)
ans = 0
for i in range(K - 1, N + 1):
    ans += ruiMax[i] - ruiMin[i] + 1
    ans %= MOD
print(ans)
