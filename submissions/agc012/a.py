N = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(N, 3 * N, 2):
    ans += a[i]

print(ans)
