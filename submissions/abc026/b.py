import math
N = int(input())
rLst = list(int(input()) for i in range(N))
ans = 0
rLst.sort(reverse=True)
for i in range(N):
    if i % 2 == 0:
        ans += rLst[i] ** 2
    else:
        ans -= rLst[i] ** 2

print(ans * math.pi)
