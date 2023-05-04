N = int(input())
a = list(map(int, input().split()))
total = sum(a)

ans = total - 2 * sum(a[1:-1:2])
print(ans)
for i in range(1, N):
    ans = 2 * a[i - 1] - ans
    print(ans)
