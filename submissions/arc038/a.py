N = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)
ans = 0
for i in range(0, N, 2):
    ans += a[i]

print(ans)
