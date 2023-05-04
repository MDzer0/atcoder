n, m = map(int, input().split())
ans = 0
tmp = 0.5
n = n % 12
tyoushin = 6
tanshin = 30

if n == 0:
    ans = (m * tyoushin) - (m * tmp)
elif m == 0:
    ans = n * tanshin
else:
    ans = abs(((n * tanshin) + (tmp * m)) - (m * tyoushin))

if ans > 180:
    print(360 - ans)
else:
    print(ans)
