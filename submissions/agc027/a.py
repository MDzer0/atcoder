N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
cnt = 0
for i in range(N - 1):
    if x >= a[i]:
        x -= a[i]
        cnt += 1
    else:
        break
if x == a[-1]:
    cnt += 1

print(cnt)
