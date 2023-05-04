nisu = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ans = 0
m1, d1 = map(int, input().split())
m2, d2 = map(int, input().split())
if m1 == m2:
    ans = d2 - d1
else:
    ans = nisu[m1 - 1] - d1
    for i in range(m1, m2 - 1):
        ans += nisu[i]
    ans += d2
print(ans)
