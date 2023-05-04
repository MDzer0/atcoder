a = list(map(int, input().split()))
ans = 10 ** 30
for i in range(3):
    tmp = (a[i] // 2) * a[i - 1] * a[i - 2]
    total = a[i] * a[i - 1] * a[i - 2]
    ans = min(ans, total - (2 * tmp))

print(ans)
