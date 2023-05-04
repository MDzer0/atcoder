N, T = map(int, input().split())

ans = 1001
tmp = 1001

for i in range(N):
    ansT, tmpT = map(int, input().split())
    if T >= tmpT:
        ans = min(ans, ansT)

if ans == 1001:
    print('TLE')
else:
    print(ans)
