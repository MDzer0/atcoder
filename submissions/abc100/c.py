N = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(N):
    while True:
        if a[i] % 2 == 0:
            ans += 1
            a[i] = a[i] // 2
        else:
            break

print(ans)
