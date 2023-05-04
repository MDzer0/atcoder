N, A, B = map(int, input().split())
v, m = divmod(N, A + B)
ans = v * A
if m >= A:
    ans += A
else:
    ans += m
print(ans)
