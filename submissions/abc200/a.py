N = int(input())
ans = 1
m, d = divmod(N, 100)

if d == 0:
    ans += m - 1
else:
    ans += m
print(ans)
