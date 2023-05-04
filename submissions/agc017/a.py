N, P = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    a[i] = a[i] % 2

g = a.count(1)
if g == 0:
    if P == 0:
        ans = 2 ** N
else:
    ans = 2 ** (N - 1)

print(ans)
