N = int(input())
a = []
b = []
ans = 10 ** 19
for i in range(N):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
    ans = min(ans, x + y)

for i in range(N):
    tmpb = 10 ** 18
    for j in range(N):
        if i == j: continue
        tmpb = min(tmpb, b[j])
    ans = min(ans, max(a[i], tmpb))
print(ans)
