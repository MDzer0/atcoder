N = int(input())
a = [int(input()) for _ in range(N)]
ans = 0
for i in range(N):
    cnt, mod = divmod(a[i], 2)
    ans += cnt
    if i < N - 1 and a[i + 1] != 0:
        a[i + 1] += mod

print(ans)
