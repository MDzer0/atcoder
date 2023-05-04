N = int(input())
a = list(map(int, input().split()))
alst = [0] * 200005
cmb1 = [0] * 200005

for i in range(N):
    alst[a[i]] += 1

for i in range(N):
    cmb1[i + 1] = cmb1[i] + ((alst[i + 1] * (alst[i + 1] - 1)) // 2)

for i in range(N):
    tmp1 = (alst[a[i]] * (alst[a[i]] - 1)) // 2
    tmp2 = ((alst[a[i]] - 1) * (alst[a[i]] - 2)) // 2
    ans = cmb1[N] - tmp1 + tmp2
    print(ans)
