N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, N):
    if a[i - 1] == a[i]:
        ans += 1
        a[i] = 0

print(ans)
