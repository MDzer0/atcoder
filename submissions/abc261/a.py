a = [0] * 1000
l1, r1, l2, r2 = map(int, input().split())
a[l1] += 1
a[r1] -= 1
a[l2] += 1
a[r2] -= 1
ans = 0
for i in range(999):
  if a[i] >= 2:
    ans += 1
  a[i+1] += a[i]
print(ans)
