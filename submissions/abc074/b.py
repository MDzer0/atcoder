N = int(input())
K = int(input())

xList = list(map(int, input().split()))

ans = 0
for i in xList:
    xtmp = 2 * i
    ytmp = abs(i - K) * 2
    ans += min(xtmp, ytmp)
print(ans)
