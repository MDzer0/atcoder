L, R = map(int, input().split())
ans = 0

f = [0] * (R + 1)
for i in range(R, 1, -1):
    tmp = R // i - (L - 1) // i
    f[i] = tmp ** 2
    for j in range(2 * i, R + 1, i):
        f[i] -= f[j]
    ans += f[i]

for i in range(max(L, 2), R + 1):
    ans -= (R // i) * 2 - 1
print(ans)
