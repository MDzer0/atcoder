N = int(input())
A = list(map(int, input().split()))
ans = 0
maxcnt = 0
for i in range(2, max(A) + 1):
    tmpcnt = 0
    for j in A:
        if j % i == 0:
            tmpcnt += 1
    if tmpcnt >= maxcnt:
        maxcnt = tmpcnt
        ans = i
print(ans)
