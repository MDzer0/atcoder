from collections import defaultdict

N, K = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
d = defaultdict(int)
for i in range(N):
    d[a[i]] += 1

ans = 0
for i in range(K):
    tmp = 0
    nexttmp = 0
    if d[0] == 0: break
    for j in d.keys():
        if d[j] == 0: break
        if j != nexttmp: break
        tmp = j + 1
        d[j] -= 1
        nexttmp += 1
    if tmp == 0: break
    ans += tmp

print(ans)
