N = int(input())
xy = [[0] * (1501) for _ in range(1501)]
for i in range(N):
    x, y = map(int, input().split())
    xy[x][y] += 1

for i in range(1, 1501):
    for j in range(1500):
        xy[i][j + 1] += xy[i][j]

for i in range(1, 1501):
    for j in range(1500):
        xy[j + 1][i] += xy[j][i]

Q = int(input())
for i in range(Q):
    a, b, c, d = map(int, input().split())
    ans = xy[a - 1][b - 1] + xy[c][d] -\
        xy[a - 1][d] - xy[c][b - 1]
    print(ans)
