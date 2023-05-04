N, K = map(int, input().split())

ans = 0

for i in range(2, 2 * N + 1):
    cnt1 = 0
    cnt2 = 0
    if 2 <= i - K <= 2 * N and i <= N:
        cnt1 = (i - 1)
        if i - K <= N:
            cnt2 = (i - K - 1)
        elif i - K < 2 * N:
            cnt2 = N - abs(N - i + K + 1)
        else:
            cnt2 = 1
    elif 2 <= i - K <= 2 * N and N < i <= 2 * N:
        cnt1 = N - abs(N - i + 1)
        if i - K <= N:
            cnt2 = (i - K - 1)
        elif i - K < 2 * N:
            cnt2 = N - abs(N - i + K + 1)
        else:
            cnt2 = 1
    ans += cnt1 * cnt2
print(ans)
