K, T = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
amax = a[-1]
asum = sum(a[:-1])
ans = 0
if T == 1:
    ans = K - 1
else:
    ans = max(amax - asum - 1, 0)
print(ans)
