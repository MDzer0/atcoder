N, K = map(int, input().split())
a = [int(input()) for _ in range(N)]
rui = [0] * N
rui[0] = 1
for i in range(1, N):
    if a[i - 1] < a[i]:
        rui[i] = rui[i - 1] + 1
    else:
        rui[i] = rui[i - 1] - 1

ans = 0
for i in range(N - K + 1):
    if rui[i + K - 1] - K + 1 == rui[i]:
        ans += 1

print(ans)
