N = int(input())
a = list(map(int, input().split()))
rui = [0] * (N + 1)
for i in range(N):
    rui[i + 1] = rui[i] + a[i]
ans = 0
for i in range(N):
    for j in range(N - i):
        ans = max(ans, rui[j + i + 1] - rui[j])
    print(ans)
