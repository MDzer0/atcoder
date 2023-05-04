N, M = map(int, input().split())
lrs = [list(map(int, input().split())) for _ in range(N)]
imos = [0] * (M + 1)

ans = 0
for i in range(N):
    imos[lrs[i][0] - 1] += lrs[i][2]
    imos[lrs[i][1]] -= lrs[i][2]
    ans += lrs[i][2]

for i in range(1, M + 1):
    imos[i] += imos[i - 1]

print(ans - min(imos[:-1]))
