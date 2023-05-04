import bisect
N, T = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]
sabun = [0] * N
total = 0
for i in range(N):
    sabun[i] = ab[i][0] - ab[i][1]
    total += ab[i][0]

sabun.sort(reverse=True)
rui = [0] * (N + 1)
for i in range(N):
    rui[i + 1] = rui[i] + sabun[i]

if total <= T:
    print(0)
    exit()
tmp = total - T
index = bisect.bisect_left(rui, tmp)

if len(rui) == index:
    print(-1)
else:
    print(index)
