D = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

total = 0
ans = 10 ** 19
for i in range(D):
    total += a[i]
    if total >= b[i]:
        ans = min(ans, b[i])

if ans == 10 ** 19:
    print(-1)
else:
    print(ans)
