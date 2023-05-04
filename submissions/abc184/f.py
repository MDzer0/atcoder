from bisect import bisect_right as right

N, T = map(int, input().split())
harf = N // 2
a = list(map(int, input().split()))
harflst = [0] * (1 << harf)
for i in range(1 << harf):
    for j in range(harf):
        if i >> j & 1:
            harflst[i] += a[j]
harflst.sort()

ans = 0
for i in range(1 << (N - harf)):
    tmp = 0
    for j in range((N - harf)):
        if i >> j & 1:
            tmp += a[harf + j]
    if tmp > T:
        continue
    index = right(harflst, T - tmp) - 1
    ans = max(ans, harflst[index] + tmp)

print(ans)
