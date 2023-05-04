import bisect

n = int(input())
f = [0, 1]
for i in range(100):
    f.append(f[-1] + f[-2])
ans = 0
while n:
    ans += 1
    n -= f[bisect.bisect_left(f, n + 0.5) - 1]
print(ans)
