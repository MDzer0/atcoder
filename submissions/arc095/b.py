import bisect

n = int(input())
a = list(map(int, input().split()))
if n == 2:
    print(max(a), min(a))
    exit()

a.sort()
ans1 = a[-1]
tmp = ans1 // 2
index = bisect.bisect_left(a, tmp)
tmp1 = abs(tmp - a[index - 1])
tmp2 = abs(tmp - a[index])
if tmp1 < tmp2:
    ans2 = index - 1
else:
    ans2 = index

print(ans1, a[ans2])
