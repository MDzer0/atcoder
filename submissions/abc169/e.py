N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]

l = sorted(ab, key=lambda x: x[0])
r = sorted(ab, key=lambda x: x[1])

if N % 2 == 0:
    maxab = ab[(N // 2) - 1][1]
    minab = ab[N // 2][0]
    x1 = (l[(N // 2) - 1][0] + l[N // 2][0])
    x2 = (r[(N // 2) - 1][1] + r[N // 2][1])
    print(x2 - x1 + 1)

else:
    print(r[N // 2][1] - l[N // 2][0] + 1)
