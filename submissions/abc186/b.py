from collections import defaultdict

H, W = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(H)]

d = defaultdict(int)
for i in range(H):
    for j in range(W):
        d[a[i][j]] += 1

d = list(d.items())
d.sort()
mincnt = d[0][0]
ans = 0
for i in range(H):
    for j in range(W):
        if mincnt != a[i][j]:
            ans += a[i][j] - d[0][0]

print(ans)
