import bisect
N = int(input())
l = list(map(int, input().split()))
ans = 0
tmp = 0
l.sort()
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        tmp = bisect.bisect_left(l, l[i] + l[j])
        ans += tmp - j - 1

print(ans)
