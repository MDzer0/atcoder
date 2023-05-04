N, L = map(int, input().split())
xa = [list(map(int, input().split())) for _ in range(N)]

top = 10 ** 20
under = 0
ans = 10 ** 21

while top - under > 1:
    mid = (top + under) // 2
    tmp = mid
    for i in range(N):
        tmp -= xa[i][1]
        if tmp < 0: break
        if i != N - 1:
            tmp = min(mid, tmp + xa[i + 1][0] - xa[i][0])

    if tmp >= 0:
        ans = min(ans, mid)
        top = mid
    else:
        under = mid

print(ans)
