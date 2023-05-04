ab = list(map(int, input().split()))
a = ab[:3]
b = ab[3:]
a.sort(), b.sort()
ans = 0

for i in range(3):
    ans += abs(a[i] - b[i])
print(ans)
